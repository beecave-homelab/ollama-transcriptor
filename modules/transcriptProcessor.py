import os
import re
from typing import List

def check_file_type(file_name: str) -> bool:
    return file_name.endswith('.txt') or file_name.endswith('.md')

def read_file_content(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def count_words(content: str) -> int:
    return len(content.split())

def split_content(content: str, max_words: int = 1000) -> List[str]:
    words = content.split()
    segments = [' '.join(words[i:i + max_words]) for i in range(0, len(words), max_words)]
    return segments

def process_content(content: str, max_words: int = 1000) -> List[str]:
    if count_words(content) > max_words:
        return split_content(content, max_words)
    return [content]

def handle_stream(response):
    return ''.join(chunk['choices'][0]['delta']['content'] for chunk in response if 'choices' in chunk and 'delta' in chunk['choices'][0])