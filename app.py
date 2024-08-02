import gradio as gr
import os
import sys
import logging
from typing import List
from dotenv import load_dotenv
from modules.findMarkdown import extract_markdown_segments, process_transcripts_folder, handle_stream

# Load environment variables
load_dotenv()

# Environment-specific settings
API_MODEL = os.getenv("API_MODEL", "qwen2:7b-instruct-q5_K_S")
SYSTEM_MESSAGE_FILE = os.getenv("SYSTEM_MESSAGE_FILE", "system-message/clean_transcript/system.md")
TRANSCRIPTS_FOLDER = os.getenv("TRANSCRIPTS_FOLDER", "transcripts")
CLEANED_TRANSCRIPTS_FOLDER = os.getenv("CLEANED_TRANSCRIPTS_FOLDER", "cleaned-transcripts")

# Add the modules directory to the system path
script_dir = os.path.dirname(__file__)
modules_path = os.path.abspath(os.path.join(script_dir, 'modules'))
sys.path.append(modules_path)

# Set up logging
logging.basicConfig(filename=os.path.join(script_dir, 'logs', 'code_extraction.log'), level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info(f"sys.path: {sys.path}")

def get_system_message(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"An error occurred while reading the system message file {file_path}", exc_info=True)
        raise

def append_to_cleaned_transcript(file_name: str, content: str) -> None:
    if not os.path.exists(CLEANED_TRANSCRIPTS_FOLDER):
        os.makedirs(CLEANED_TRANSCRIPTS_FOLDER)
    
    cleaned_file_path = os.path.join(CLEANED_TRANSCRIPTS_FOLDER, file_name)
    with open(cleaned_file_path, 'a') as file:
        file.write(content + '\n')

def process_file(file_name, content):
    code_blocks, num_blocks = extract_markdown_segments(content)

    results = []
    results.append(f"Found {num_blocks} markdown segments in the audio-to-text transcription from {file_name}.\n")
    results.append("—" * 30)

    system_message_content = get_system_message(os.path.join(script_dir, SYSTEM_MESSAGE_FILE))

    cleaned_segments = []

    for idx, code in enumerate(code_blocks, start=1):
        system_message = {'role': 'system', 'content': system_message_content}
        user_message = {'role': 'user', 'content': code.strip()}
        messages = [system_message, user_message]
        response = ollama.chat(model=API_MODEL, messages=messages, stream=True)
        
        response_content = []
        for chunk in response:
            response_content.append(chunk['message']['content'])
            results.append(chunk['message']['content'])

        cleaned_content = ''.join(response_content)
        append_to_cleaned_transcript(file_name, cleaned_content)
        cleaned_segments.append(cleaned_content)
        results.append("\n" + "-"*50 + "\n")

    return "\n".join(results), "\n".join(cleaned_segments)

def main():
    markdown_files: List[str] = process_transcripts_folder(TRANSCRIPTS_FOLDER)
    results = []
    cleaned = []
    for file_name in markdown_files:
        result, cleaned_segment = process_file(file_name)
        results.append(result)
        cleaned.append(cleaned_segment)
    return "\n".join(results), "\n".join(cleaned)

def gradio_interface():
    with gr.Blocks() as demo:
        gr.Markdown(
            """
            # Markdown Processing Tool
            Upload your transcript files and process them to extract and clean markdown segments.
            """
        )

        with gr.Row():
            with gr.Column(scale=1):
                file_input = gr.File(label="Upload Transcripts", file_count="multiple", file_types=["text"])
                process_button = gr.Button("Process Files")

            with gr.Column(scale=2):
                output_text = gr.Textbox(label="Output", lines=20)
                cleaned_text = gr.Textbox(label="Cleaned Segments", lines=20)

        def process_transcripts(files):
            results = []
            cleaned_results = []
            for file in files:
                file_name = os.path.basename(file.name)
                file_content = file.value.decode("utf-8")
                result, cleaned_segment = process_file(file_name, file_content)
                results.append(result)
                cleaned_results.append(cleaned_segment)
            return "\n".join(results), "\n".join(cleaned_results)

        process_button.click(process_transcripts, inputs=[file_input], outputs=[output_text, cleaned_text])

    return demo

if __name__ == "__main__":
    demo = gradio_interface()
    demo.launch()