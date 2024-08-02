import gradio as gr
import os
import sys
import logging
from typing import List
from dotenv import load_dotenv
from modules.transcriptProcessor import check_file_type, read_file_content, process_content, handle_stream
from openai import OpenAI

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")
API_MODEL = os.getenv("API_MODEL")
SYSTEM_MESSAGE_FILE = os.getenv("SYSTEM_MESSAGE_FILE")
TRANSCRIPTS_FOLDER = os.getenv("TRANSCRIPTS_FOLDER")
CLEANED_TRANSCRIPTS_FOLDER = os.getenv("CLEANED_TRANSCRIPTS_FOLDER")
MAX_TOKENS = int(os.getenv("MAX_TOKENS"))
TEMPERATURE = float(os.getenv("TEMPERATURE"))

# Set up logging
logging.basicConfig(filename='code_extraction.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

openai_client = OpenAI(api_key=API_KEY, base_url=OPENAI_BASE_URL)

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
    cleaned_file_path = os.path.join(CLEANED_TRANSCRIPTS_FOLDER, file_name)
    os.makedirs(os.path.dirname(cleaned_file_path), exist_ok=True)
    with open(cleaned_file_path, 'a') as file:
        file.write(content + '\n')

def process_file(file_name, content, update_output, update_cleaned):
    segments = process_content(content)
    results = []
    cleaned_segments = []

    system_message_content = get_system_message(SYSTEM_MESSAGE_FILE)

    for idx, segment in enumerate(segments, start=1):
        messages = [
            {"role": "system", "content": system_message_content},
            {"role": "user", "content": segment.strip()}
        ]
        response = openai_client.chat.completions.create(
            model=API_MODEL,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            stream=True
        )
        
        cleaned_content = ""
        for chunk in response:
            if 'choices' in chunk and 'delta' in chunk['choices'][0]:
                part = chunk['choices'][0]['delta']['content']
                cleaned_content += part
                update_cleaned(cleaned_content)
        
        append_to_cleaned_transcript(file_name, cleaned_content)
        cleaned_segments.append(cleaned_content)
        results.append(cleaned_content)
        update_output("\n".join(results))
    
    return "\n".join(results), "\n".join(cleaned_segments)

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

        def display_file_content(file):
            file_name = os.path.basename(file.name)
            with open(file.name, "r", encoding="utf-8") as f:
                file_content = f.read()
            return file_content

        def process_transcripts(files):
            results = []
            cleaned_results = []
            for file in files:
                file_name = os.path.basename(file.name)
                with open(file.name, "r", encoding="utf-8") as f:
                    file_content = f.read()
                if check_file_type(file_name):
                    update_output = lambda content: output_text.update(value=content)
                    update_cleaned = lambda content: cleaned_text.update(value=content)
                    result, cleaned_segment = process_file(file_name, file_content, update_output, update_cleaned)
                    results.append(result)
                    cleaned_results.append(cleaned_segment)
            return "\n".join(results), "\n".join(cleaned_results)

        file_input.change(display_file_content, inputs=file_input, outputs=output_text)
        process_button.click(process_transcripts, inputs=[file_input], outputs=[output_text, cleaned_text])

    return demo

if __name__ == "__main__":
    demo = gradio_interface()
    demo.launch()