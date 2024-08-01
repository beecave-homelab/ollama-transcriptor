# ollama-transcriptor

Send chunks of 1000 words from a audio-to-text transcript to Ollama

## Project structure
```md
/Projects/ollama-transcriptor
├── app.py
├── cleaned-transcripts
├── diagnostics.py
├── LICENSE
├── modules
│  ├── __init__.py
│  ├── findMarkdown.py
│  └── messageColor.py
├── README.md
├── system-message
│  └── clean_transcript
└── transcripts
   └── 2024-07-29-Transcript - Introducing Substrate—An Open-source Framework for Human Understanding, Meaning, and Progress.md
```

# TO DO
- Set system message from `.md` file in `./system-message/clean_transcript` with the name `system.md`
- Add support for choosing model by calling the OLLAMA_MODEL_API variable with the default value of `http://localhost:11434/v1/models`
- Add support choosing what system message should be used by adding support of all the folder names that are present in: `./system_message`
- Add support to call the `find-markdown.py` script from the `./find-markdown` folder and send every segment of the transcript as a message to the model. Append the response to the message to `./response` folder with the name of the input file used in `./find-markdown/transcripts` folder.
 