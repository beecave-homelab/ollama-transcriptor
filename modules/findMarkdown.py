import re
import os

def extract_markdown_segments(file_path: str):
    try:
        # Read the user message from a file
        with open(file_path, 'r') as file:
            user_message_content = file.read()

        # Extract code blocks from the user message
        code_blocks = re.findall(r'```md(.*?)```', user_message_content, re.DOTALL)
        num_blocks = len(code_blocks)

        return code_blocks, num_blocks
    except FileNotFoundError:
        raise
    except Exception as e:
        raise

def process_transcripts_folder(folder_path: str):
    try:
        files = [f for f in os.listdir(folder_path) if f.endswith('.md') or f.endswith('.txt')]
        if not files:
            return ['klas24-session-2024-01-29-whisper-large.md']
        return files
    except Exception as e:
        raise

def handle_stream(response):
    for chunk in response:
        print(chunk['message']['content'], end='')