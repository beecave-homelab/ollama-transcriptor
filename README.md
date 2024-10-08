# Ollama Transcriptor | A Simple Transcript Text Cleaner

Ollama Transcriptor is a Python application designed to take transcripts generated by Whisper and clean them for spelling, grammar, punctuation errors, and line breaks. The application uses the OpenAI API to communicatie with a local or remote Ollama server to ensure high-quality text processing. It provides a user-friendly Gradio interface for uploading and processing transcripts, making it easy to generate polished text from raw transcriptions.

The application can handle large text inputs by automatically cutting them into chunks (each containing up to 2048 words) before processing. After cleaning, the text is exported into a `.txt` file for downloading and is also displayed in the web interface for easy copying.

## Table of Contents
- [Badges](#badges)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contributing](#contributing)

## Badges
![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Project overview
```md
ollama-transcriptor/
├── cleaned-transcripts/
├── docker-compose.yaml
├── Dockerfile
├── LICENSE
├── modules
├── README.md
├── requirements.txt
├── src/
│  ├── app.py
│  └── modules/
│     ├── messageColor.py
│     └── transcriptProcessor.py
├── system-message/
│  ├── clean_text/
│  │  └── clean_text.md
│  ├── clean_text_v2/
│  │  └── clean_text_v2.md
│  ├── clean_transcript/
│  │  └── clean_transcript.md
│  └── clean_transcript_v2/
│     └── clean_transcript_v2.md
├── testing/
│  └── diagnostics.py
```

## Installation

To install the Ollama Transcriptor, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/beecave-homelab/ollama-transcriptor.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ollama-transcriptor
    ```
3. Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

   The main dependencies are:
   - `openai`
   - `gradio`
   - `python-dotenv`
   - `rich`

4. Set up environment variables by creating a `.env` file in the project directory with the following variables. You can adjust the values to your liking or copy the the default values frok the example file with `cp .env.example .env`:
    ```env
    # OpenAI API credentials
    OPENAI_API_KEY=
    OPENAI_BASE_URL=http://host.docker.internal:11434/v1

    # Default model configuration
    DEFAULT_OPENAI_MODEL=qwen2:7b-instruct-q5_K_S

    # System message directory
    SYSTEM_MESSAGE_DIR=system-message

    # Generation parameters
    MAX_TOKENS=8192
    TEMPERATURE=0.1

    # Folder for cleaned transcripts
    CLEANED_TRANSCRIPTS_FOLDER=cleaned-transcripts
    ```

5. In the `system-message` directory you'll find different folders with different system messages. You can use (or adjust) these messages to your liking. To create a new message, create a new folder and `.md` file in the `system-message` directory.
    ```md
    system-message
    ├── clean_text
    │  └── clean_text.md
    ├── clean_text_v2
    │  └── clean_text_v2.md
    ├── clean_transcript
    │  └── clean_transcript.md
    └── clean_transcript_v2
    └── clean_transcript_v2.md
    ```
6. When running the script locally, first download the spaCy language model:
    ```bash
    python -m spacy download en_core_web_lg
    ```

## Usage

To use the Ollama Transcriptor, follow these steps:

1. Ensure that you have your `.env` file properly configured as described in the installation steps.
2. Run the application using:
    ```bash
    python src/app.py
    ```
3. A Gradio interface will launch in your web browser, allowing you to:
   - Upload transcript files generated by Whisper or input text manually.
   - Choose the OpenAI model, set the temperature, and configure other settings.
   - Process the transcript, which will be cleaned of spelling, grammar, punctuation errors, and unwanted line breaks.
   - If the input text is larger than 1,000 words, it will be automatically split into chunks before processing.
   - The cleaned transcript will be displayed in the interface and saved as a `.txt` file in the `cleaned-transcripts` directory for downloading.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.