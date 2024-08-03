import os
from openai import OpenAI
import gradio as gr
from dotenv import load_dotenv
import shutil

# Load environment variables
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

# Ensure the uploads directory exists
UPLOAD_FOLDER = "./uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def predict(message, history):
    history_openai_format = [{"role": "system", "content": system_message}]
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human})
        if assistant is not None:
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
            partial_message += chunk.choices[0].delta.content
            yield partial_message

def add_message(history, files, text):
    if files is not None:
        for file in files:
            file_path = os.path.join(UPLOAD_FOLDER, os.path.basename(file.name))
            shutil.copy(file.name, file_path)
            with open(file_path, 'r') as f:
                file_content = f.read()
            history.append((f"File uploaded: {file.name}\nContent:\n{file_content}", None))
    if text is not None:
        history.append((text, None))
    return history, gr.update(value="", interactive=True)

def bot_response(history):
    if not history:
        raise ValueError("History is empty, cannot generate a response.")
    
    # Combine all previous messages and file contents
    combined_message = "\n".join([entry[0] for entry in history])
    assistant_response = list(predict(combined_message, history[:-1]))[-1]
    history[-1][1] = assistant_response
    return history

with gr.Blocks(fill_height=True) as demo:
    chatbot = gr.Chatbot(
        elem_id="chatbot",
        bubble_full_width=False,
        scale=1,
    )

    chat_input = gr.Textbox(
        interactive=True,
        placeholder="Enter message...",
        show_label=False
    )

    file_input = gr.File(
        file_count="multiple",
        type="filepath",
        interactive=True,
        show_label=False
    )

    chat_msg = chat_input.submit(add_message, [chatbot, file_input, chat_input], [chatbot, chat_input])
    file_msg = file_input.change(add_message, [chatbot, file_input, chat_input], [chatbot, chat_input])
    bot_msg = chat_msg.then(bot_response, chatbot, chatbot, api_name="bot_response")
    bot_msg.then(lambda: gr.update(value="", interactive=True), None, [chat_input])

demo.launch()