import os
from openai import OpenAI
import gradio as gr
from dotenv import load_dotenv
import shutil
from modules.transcriptProcessor import check_file_type, read_file_content, process_content

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL")
MODEL = os.getenv("OPENAI_MODEL")
SYSTEM_MESSAGE_FILE = os.getenv("SYSTEM_MESSAGE_FILE")
MAX_TOKENS = int(os.getenv("MAX_TOKENS"))
TEMPERATURE = float(os.getenv("TEMPERATURE"))

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# Check if the system message file exists
if not os.path.exists(SYSTEM_MESSAGE_FILE):
    raise FileNotFoundError(f"System message file not found: {SYSTEM_MESSAGE_FILE}")

# Read the system message from file
with open(SYSTEM_MESSAGE_FILE, 'r') as file:
    system_message = file.read()

# Ensure the uploads directory exists
UPLOAD_FOLDER = "./uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def predict(segment, history):
    history_openai_format = [{"role": "system", "content": system_message}]
    history_openai_format.append({"role": "user", "content": segment})
  
    response = client.chat.completions.create(
        model=MODEL,
        messages=history_openai_format,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        stream=True
    )

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            partial_message += chunk.choices[0].delta.content
            yield partial_message

def process_transcripts(files):
    history = []
    full_history = ""
    if files is not None:
        for file in files:
            file_path = os.path.join(UPLOAD_FOLDER, os.path.basename(file.name))
            shutil.copy(file.name, file_path)
            if check_file_type(file_path):
                file_content = read_file_content(file_path)
                segments = process_content(file_content)
                for segment in segments:
                    output_stream = predict(segment, history)
                    assistant_response = ""
                    for output in output_stream:
                        assistant_response += output
                        yield output, full_history
                    history.append([segment, assistant_response])
                    full_history += f"\nUser: {segment}\nAssistant: {assistant_response}\n"
            else:
                yield f"Unsupported file type: {file.name}", full_history
        yield "", full_history

with gr.Blocks(fill_height=True) as demo:
    file_input = gr.File(
        file_count="multiple",
        type="filepath",
        interactive=True,
        show_label=False,
        label="Upload Transcript Files"
    )

    stream_display = gr.Textbox(
        interactive=False,
        show_label=False,
        label="Stream Output"
    )

    history_display = gr.Textbox(
        interactive=False,
        show_label=False,
        label="History"
    )

    file_input.change(
        process_transcripts, 
        inputs=[file_input], 
        outputs=[stream_display, history_display]
    )

demo.launch()