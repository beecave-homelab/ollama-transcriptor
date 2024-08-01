# ollama-transcriptor

Send chunks of 1000 words from a audio-to-text transcript to Ollama

## Project structure
```md
/Users/elvee/Nextcloud/Projects/ollama-transcriptor
├── __init__.py
├── diagnostics.py
├── LICENSE
├── logs
│  └── code_extraction.log
├── modules
│  ├── __init__.py
│  ├── findMarkdown.py
│  └── messageColor.py
├── ollama-transcriptor.py
├── README.md
├── system-message
│  ├── __init__.py
│  └── clean_transcript
├── transcripts
│  └── __init__.py
└── venv
```

# TO DO
- Set system message from `.md` file in `./system-message/clean_transcript` with the name `system.md`
- Add support for choosing model by calling the OLLAMA_MODEL_API variable with the default value of `http://localhost:11434/v1/models`
- Add support choosing what system message should be used by adding support of all the folder names that are present in: `./system_message`
- Add support to call the `find-markdown.py` script from the `./find-markdown` folder and send every segment of the transcript as a message to the model. Append the response to the message to `./response` folder with the name of the input file used in `./find-markdown/transcripts` folder.
 