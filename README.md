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
- [X] Set system message from `.md` file in `./system-message/clean_transcript` with the name `system.md`
- [ ] Add support choosing what system message should be used by adding support of all the folder names that are present in: `./system-message`
- [X] Add support to call the `findMarkdown.py` script from the `./modules` folder and send every segment of the transcript as a message to the model. Append the response to the message to `./response` folder with the name of the input file used in `./find-markdown/transcripts` folder.
- [ ] Add support to call the `messageColor.py` script from the `./modules` folder and send every segment of the transcript as a message to the model. Append the response to every status message send to the console.
- [ ] Add support to set variables in a `.env`:
    - [ ] Add support for choosing the OLLAMA_API_SERVER variable with the default value of `http://localhost:11434/v1`. This is only usefull when also creating a webui or a script with [typer](https://github.com/tiangolo/typer). 
    - [ ] Add support for choosing model by calling the OLLAMA_MODEL_API variable with the default value of `http://localhost:11434/v1/models`. This is only usefull when also creating a webui or a script with [typer](https://github.com/tiangolo/typer). 
    - [ ] Add support for choosing the system message by calling the MODEL_SYSTEM_MESSAGE variable with the default value of `./system-message/clean_transcript/system.md`
    - [ ] Add support for choosing the transcripts folder by calling the TRANSCRIPTS_FOLDER variable with the default value of `./transcripts`
    - [ ] Add support for choosing the response folder by calling the CLEANED_TRANSRIPT variable with the default value of `./response`
- [ ] Recreate the `text-splitter.sh` script from the [text-splitter](https://github.com/beecave-homelab/text-splitter) repository in Python.
- [ ] Add support to call the `textSplitter.py` script from the `./modules` folder and cut the text into chunks of 1000 words in their own Markdown codeblock. Save them in the `./transcripts` folder.
- [ ] Add support for setting CLI arguments for all the variables used in the script (they should also be present in the `.env` file).
- [ ] Add and `.env.example` file to the repository.

