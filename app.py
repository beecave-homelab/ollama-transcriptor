import os
from openai import OpenAI
import gradio as gr

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL")
MODEL = os.getenv("OPENAI_MODEL")
SYSTEM_MESSAGE_FILE = os.getenv("SYSTEM_MESSAGE_FILE")
MAX_TOKENS = int(os.getenv("MAX_TOKENS"))
TEMPERATURE = float(os.getenv("TEMPERATURE"))

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# Read the system message from file
with open(SYSTEM_MESSAGE_FILE, 'r') as file:
    system_message = file.read()

def predict(message, history):
    history_openai_format = [{"role": "system", "content": system_message}]
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human})
        history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": message})
  
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
            partial_message = partial_message + chunk.choices[0].delta.content
            yield partial_message

gr.ChatInterface(predict).launch()