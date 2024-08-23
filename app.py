import os
from openai import OpenAI
import gradio as gr
from dotenv import load_dotenv
import shutil
from modules.transcriptProcessor import check_file_type, read_file_content
import logging
from rich.logging import RichHandler
import spacy

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL")

DEFAULT_MODEL = os.getenv("DEFAULT_OPENAI_MODEL")
MODEL_1 = os.getenv("OPENAI_MODEL_1")
MODEL_2 = os.getenv("OPENAI_MODEL_2")
MODEL_3 = os.getenv("OPENAI_MODEL_3")

SYSTEM_MESSAGE_1 = os.getenv("SYSTEM_MESSAGE_1")
SYSTEM_MESSAGE_2 = os.getenv("SYSTEM_MESSAGE_2")
SYSTEM_MESSAGE_3 = os.getenv("SYSTEM_MESSAGE_3")

MAX_TOKENS = int(os.getenv("MAX_TOKENS"))
TEMPERATURE = float(os.getenv("TEMPERATURE"))
CLEANED_TRANSCRIPTS_FOLDER = os.getenv("CLEANED_TRANSCRIPTS_FOLDER", "cleaned-transcripts")

# Logging setup
logging.basicConfig(level="DEBUG", handlers=[RichHandler()])
logger = logging.getLogger("transcript_processor")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# Load the spaCy language model for chunking text
nlp = spacy.load("en_core_web_lg")

# Ensure the uploads and cleaned transcripts directories exist
UPLOAD_FOLDER = "./uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(CLEANED_TRANSCRIPTS_FOLDER):
    os.makedirs(CLEANED_TRANSCRIPTS_FOLDER)

# Ensure system message files exist
for system_message_file in [SYSTEM_MESSAGE_1, SYSTEM_MESSAGE_2, SYSTEM_MESSAGE_3]:
    if system_message_file and not os.path.exists(system_message_file):
        os.makedirs(os.path.dirname(system_message_file), exist_ok=True)
        with open(system_message_file, 'w') as file:
            file.write("")

def nest_sentences(document, max_length=MAX_TOKENS):
    """
    Break down a document into manageable chunks of sentences where each chunk is under max_length characters.
    
    Parameters:
    - document (str): The input text document to be processed.
    - max_length (int): The maximum character length for each chunk of sentences.
    
    Returns:
    - list: A list where each element is a group of sentences that together are less than max_length characters.
    """
    nested = []  # List to hold all chunks of sentences
    sent = []    # Temporary list to hold sentences for a current chunk
    length = 0   # Counter to keep track of the character length of the current chunk
    doc = nlp(document)  # Process the document using spaCy to tokenize into sentences
    
    for sentence in doc.sents:
        length += len(sentence.text)
        if length < max_length:
            sent.append(sentence.text)
        else:
            nested.append(' '.join(sent))  # Join sentences in the chunk and add to the nested list
            sent = [sentence.text]  # Start a new chunk with the current sentence
            length = len(sentence.text)  # Reset the length counter to the length of the current sentence

    if sent:  # Don't forget to add the last chunk if it's not empty
        nested.append(' '.join(sent))

    return nested

def predict(segment, history, model, max_tokens, temperature, system_message):
    history_openai_format = [{"role": "system", "content": system_message}]
    history_openai_format.append({"role": "user", "content": segment})

    response = client.chat.completions.create(
        model=model,
        messages=history_openai_format,
        max_tokens=max_tokens,
        temperature=temperature,
        stream=True
    )

    full_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            full_message += chunk.choices[0].delta.content
            yield full_message

def transcript_cleaning_process_info(text, files, model, max_tokens, temperature, system_message):
    history = []
    output_display_content = "Transcript text cleaning has started.\n\n"
    cleaned_content = ""

    combined_content = ""
    cleaned_file_name = "cleaned_transcript.txt"

    # Handle file inputs
    if files is not None and len(files) > 0:
        file_path = files[0].name if isinstance(files[0], gr.File) else files[0]
        if check_file_type(file_path):
            file_type = os.path.splitext(file_path)[1]
            file_content = read_file_content(file_path)
            file_name = os.path.basename(file_path)
            cleaned_file_name = file_name  # Save cleaned transcript with the same name
            combined_content += file_content + "\n"
            output_display_content += f"Uploaded a {file_type} file.\n"
            output_display_content += f"{file_name} was uploaded for text cleaning.\n"
            word_count = len(file_content.split())
            output_display_content += f"The transcript of {file_name} contains {word_count} words.\n"
        else:
            output_display_content = f"Unsupported file type: {file_path}\n"
            yield output_display_content, ""
    elif text is not None and text.strip():
        combined_content += text
        word_count = len(text.split())
        output_display_content += f"The transcript contains {word_count} words.\n"

    # Process the combined content if there's any
    if combined_content.strip():
        segments = nest_sentences(combined_content, max_length=MAX_TOKENS)
        num_segments = len(segments)
        output_display_content += f"The transcript will be sent in {num_segments} segments.\n"

        cleaned_file_path = os.path.join(CLEANED_TRANSCRIPTS_FOLDER, cleaned_file_name)
        with open(cleaned_file_path, 'w') as cleaned_file:
            for i, segment in enumerate(segments):
                output_display_content += f"Sending segment {i + 1} of {num_segments}.\n"
                yield output_display_content, ""
                output_stream = predict(segment, history, model, max_tokens, temperature, system_message)
                assistant_response = ""
                for output in output_stream:
                    assistant_response = output  # Accumulate the complete response
                history.append([segment, assistant_response])
                cleaned_file.write(assistant_response + "\n")  # Write the full response to the file
                output_display_content += f"Cleaned text for segment {i + 1} of {num_segments}.\n"

        output_display_content += "The text cleaning process has finished.\n"
        with open(cleaned_file_path, 'r') as cleaned_file:  # Read the cleaned file content
            cleaned_content = cleaned_file.read()
    else:
        output_display_content += "No valid content to process.\n"

    yield output_display_content, cleaned_content  # Yielding final results

def read_system_message(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    return ""

def create_gradio_interface():
    theme = gr.themes.Base(
        primary_hue="green",
        secondary_hue="stone",
        neutral_hue="gray",
        font=("Helvetica", "sans-serif"),
    ).set(
        body_background_fill="linear-gradient(to right, #2c5e1a, #4a3728)",
        body_background_fill_dark="linear-gradient(to right, #1a3c0f, #2e2218)",
        button_primary_background_fill="#4a3728",
        button_primary_background_fill_hover="#5c4636",
        block_title_text_color="#e0d8b0",
        block_label_text_color="#c1b78f",
    )

    with gr.Blocks(theme=theme) as demo:
        gr.Markdown(
            """
            # Transcript Processor
            Upload your transcript files for processing or enter text.
            """
        )

        with gr.Row():
            with gr.Column(scale=2):
                gr.Markdown(
                    """
                    ### Text to transcribe
                    """
                )

                # Use Textbox for text input
                text_input = gr.Textbox(
                    interactive=True,
                    placeholder="Enter the transcript text.",
                    show_label=False
                )

                # Use File component for file uploads
                file_input = gr.File(
                    file_count="multiple",
                    label="Upload transcript files"
                )

                gr.Markdown(
                    """
                    ### Cleaned transcript
                    Your cleaned and reformatted transcript will be available below.
                    """
                )

                cleaned_transcript_display = gr.Textbox(
                    interactive=False,
                    show_label=True,
                    label="Cleaned transcript",
                    show_copy_button=True
                )

        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown(
                    """
                    ### Processed Output
                    The processed text and responses will be displayed here.
                    """
                )
                output_display = gr.Textbox(
                    interactive=False,
                    show_label=False,
                    label="Output"
                )

                gr.Markdown(
                    """
                    ### Model configuration
                    Select the model, set the context length, temperature and which system message to use.
                    """
                )
                
                with gr.Accordion("Model Configuration", open=False):
                    model_choice = gr.Dropdown(
                        choices=[DEFAULT_MODEL, MODEL_1, MODEL_2, MODEL_3],
                        value=DEFAULT_MODEL,
                        label="Model"
                    )
                    temperature = gr.Slider(minimum=0, maximum=1, value=float(TEMPERATURE), label="Temperature")
                    max_tokens = gr.Slider(minimum=1, maximum=8192, step=1, value=int(MAX_TOKENS), label="Max Tokens")

                    system_message_files = {
                        os.path.basename(SYSTEM_MESSAGE_1): SYSTEM_MESSAGE_1,
                        os.path.basename(SYSTEM_MESSAGE_2): SYSTEM_MESSAGE_2,
                        os.path.basename(SYSTEM_MESSAGE_3): SYSTEM_MESSAGE_3
                    }
                    system_message_dropdown = gr.Dropdown(
                        choices=list(system_message_files.keys()),
                        label="Select System Message",
                        value=list(system_message_files.keys())[0]
                    )

                    system_message_input = gr.Textbox(
                        value=read_system_message(system_message_files[list(system_message_files.keys())[0]]),
                        label="System Message",
                        placeholder="System message content...",
                        lines=10,
                        interactive=False
                    )

                    def update_system_message(file_key):
                        file_path = system_message_files[file_key]
                        return read_system_message(file_path)

                    system_message_dropdown.change(
                        update_system_message,
                        inputs=system_message_dropdown,
                        outputs=system_message_input
                    )

        # Create a button to trigger the transcript processing
        submit_button = gr.Button("Process Transcript")

        # Handle the submission using the button click
        submit_button.click(
            fn=transcript_cleaning_process_info,
            inputs=[text_input, file_input, model_choice, max_tokens, temperature, system_message_input],
            outputs=[output_display, cleaned_transcript_display]
        )

    return demo

if __name__ == "__main__":
    demo = create_gradio_interface()  # Assign the returned value to 'demo'
    demo.queue()
    demo.launch()