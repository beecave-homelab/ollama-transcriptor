import gradio as gr
import ollama
import os
import sys
import logging

# Add the modules directory to the system path
script_dir = os.path.dirname(__file__)
modules_path = os.path.abspath(os.path.join(script_dir, 'modules'))
sys.path.append(modules_path)

# Log the sys.path for debugging
logging.basicConfig(filename=os.path.join(script_dir, 'logs', 'code_extraction.log'), level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info(f"sys.path: {sys.path}")

try:
    from modules.findMarkdown import extract_markdown_segments, process_transcripts_folder, handle_stream
except ModuleNotFoundError as e:
    logging.error(f"ModuleNotFoundError: {e}")
    raise

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
    cleaned_transcripts_folder = os.path.join(script_dir, 'cleaned-transcripts')
    if not os.path.exists(cleaned_transcripts_folder):
        os.makedirs(cleaned_transcripts_folder)
    
    cleaned_file_path = os.path.join(cleaned_transcripts_folder, file_name)
    with open(cleaned_file_path, 'a') as file:
        file.write(content + '\n')

def process_transcript(file_name: str, transcript_content: str):
    code_blocks, num_blocks = extract_markdown_segments(transcript_content)

    for idx, code in enumerate(code_blocks, start=1):
        system_message_content = get_system_message(os.path.join(script_dir, 'system-message', 'clean_transcript', 'system.md'))
        system_message = {'role': 'system', 'content': system_message_content}
        user_message = {'role': 'user', 'content': code.strip()}
        messages = [system_message, user_message]
        response = ollama.chat(model='qwen2:7b-instruct-q5_K_S', messages=messages, stream=True)
        
        response_content = []
        for chunk in response:
            response_content.append(chunk['message']['content'])
        
        cleaned_content = ''.join(response_content)
        append_to_cleaned_transcript(file_name, cleaned_content)

def gradio_interface():
    with gr.Blocks() as demo:
        gr.Markdown("## Ollama Transcriptor")
        transcript_input = gr.Textbox(lines=10, placeholder="Enter or upload your transcript content here...", label="Transcript Content")
        submit_btn = gr.Button("Process Transcript", variant="primary")
        output = gr.Textbox(lines=20, placeholder="Processed content will appear here...", label="Processed Content")

        def process_input(content):
            file_name = "input_transcript.md"
            process_transcript(file_name, content)
            with open(os.path.join(script_dir, 'cleaned-transcripts', file_name), 'r') as file:
                return file.read()
        
        submit_btn.click(process_input, inputs=transcript_input, outputs=output)

    demo.launch(share=True, debug=True)

if __name__ == "__main__":
    gradio_interface()