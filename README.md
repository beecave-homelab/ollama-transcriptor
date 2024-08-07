```markdown
# ollama-transcriptor

Send chunks of 1000 words from an audio-to-text transcript to Ollama

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
│  ├── messageColor.py
│  └── transcriptProcessor.py
├── README.md
├── system-message
│  └── clean_transcript
└── transcripts
   └── 2024-07-29-Transcript - Introducing Substrate—An Open-source Framework for Human Understanding, Meaning, and Progress.md
```

## TO DO
- [x] Set system message from `.md` file in `./system-message/clean_transcript` with the name `system.md`
- [ ] Add support for choosing which system message should be used by adding support for all the folder names that are present in: `./system-message`
- [x] Add support to call the `findMarkdown.py` script from the `./modules` folder and send every segment of the transcript as a message to the model. Append the response to the message to `./response` folder with the name of the input file used in `./find-markdown/transcripts` folder.
- [ ] Add support to call the `messageColor.py` script from the `./modules` folder and send every segment of the transcript as a message to the model. Append the response to every status message sent to the console.
- [X] Add support to set variables in a `.env`:
    - [X] Add support for choosing the OLLAMA_API_SERVER variable with the default value of `http://localhost:11434/v1`. 
    - [X] Add support for choosing the model by calling the OLLAMA_MODEL_API variable with the default value of `http://localhost:11434/v1/models`. This is only useful when also creating a web UI or a script with [typer](https://github.com/tiangolo/typer). 
    - [X] Add support for choosing the system message by calling the MODEL_SYSTEM_MESSAGE variable with the default value of `./system-message/clean_transcript/system.md`
    - [X] Add support for choosing the transcripts folder by calling the TRANSCRIPTS_FOLDER variable with the default value of `./transcripts`
    - [X] Add support for choosing the response folder by calling the CLEANED_TRANSRIPT variable with the default value of `./response`
- [X] Recreate the `text-splitter.sh` script from the [text-splitter](https://github.com/beecave-homelab/text-splitter) repository in Python.
- [X] Add support to call the `textSplitter.py` script from the `./modules` folder and cut the text into chunks of 1000 words in their own Markdown code block. Save them in the `./transcripts` folder.
- [ ] Add support for setting CLI arguments for all the variables used in the script (they should also be present in the `.env` file).
- [X] Add an `.env.example` file to the repository.

IDEAS:
- [ ] Recreate the script with [typer](https://github.com/tiangolo/typer). 
- [ ] Recreate the script with [Click](https://click.palletsprojects.com/en/8.1.x/)
- [ ] Create an API with [FastAPI](https://github.com/tiangolo/fastapi).
- [X] Create a web UI with [Gradio](https://github.com/gradio-app/gradio).
- [ ] Create a web UI with [Taipy](https://github.com/Avaiga/taipy).
```