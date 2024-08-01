import ollama
import os
import sys
import logging
from typing import List

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

def main() -> None:
    """The main function."""
    
    # Load system message from file
    system_message_path = os.path.join(script_dir, 'system-message', 'clean_transcript', 'system.md')
    system_message_content = get_system_message(system_message_path)
    
    transcripts_folder = os.path.join(script_dir, 'transcripts')
    markdown_files: List[str] = process_transcripts_folder(transcripts_folder)

    for file_name in markdown_files:
        # Extract markdown segments
        code_blocks, num_blocks = extract_markdown_segments(os.path.join(transcripts_folder, file_name))

        print(f"Found {num_blocks} markdown segments in the audio-to-text transcription from {file_name}.\n")
        print("—" * 30)

        for idx, code in enumerate(code_blocks, start=1):
            # Process markdown segments
            system_message = {
                'role': 'system',
                'content': system_message_content
            }
            user_message = {
                'role': 'user',
                'content': code.strip()
            }
            messages = [system_message, user_message]
            response = ollama.chat(model='qwen2:7b-instruct-q5_K_S', messages=messages, stream=True)
            
            # Capture the response and append to cleaned transcript
            response_content = []
            for chunk in response:
                response_content.append(chunk['message']['content'])
                print(chunk['message']['content'], end='')  # Also print to console
            
            cleaned_content = ''.join(response_content)
            append_to_cleaned_transcript(file_name, cleaned_content)
            print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
