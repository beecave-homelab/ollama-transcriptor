import os
import sys
import logging
import ollama

# Add the modules directory to the system path
script_dir = os.path.dirname(__file__)
modules_path = os.path.abspath(os.path.join(script_dir, 'modules'))
sys.path.append(modules_path)

# Print sys.path for debugging
print("sys.path:")
for path in sys.path:
    print(path)

# Check if the modules directory exists and list its contents
print("\nChecking if 'modules' directory exists and its contents:")
if os.path.isdir(modules_path):
    print(f"'modules' directory exists: {modules_path}")
    print("Contents of 'modules':")
    for item in os.listdir(modules_path):
        print(item)
else:
    print(f"'modules' directory does not exist: {modules_path}")

# Check if __init__.py exists
init_file_path = os.path.join(modules_path, '__init__.py')
print(f"\nChecking if '__init__.py' exists: {init_file_path}")
if os.path.isfile(init_file_path):
    print("'__init__.py' exists")
else:
    print("'__init__.py' does not exist")

# Check if findMarkdown.py exists
find_markdown_file_path = os.path.join(modules_path, 'findMarkdown.py')
print(f"\nChecking if 'findMarkdown.py' exists: {find_markdown_file_path}")
if os.path.isfile(find_markdown_file_path):
    print("'findMarkdown.py' exists")
else:
    print("'findMarkdown.py' does not exist")

# Check if messageColor.py exists
message_color_file_path = os.path.join(modules_path, 'messageColor.py')
print(f"\nChecking if 'messageColor.py' exists: {message_color_file_path}")
if os.path.isfile(message_color_file_path):
    print("'messageColor.py' exists")
else:
    print("'messageColor.py' does not exist")

# Try importing the modules
print("\nTrying to import 'findMarkdown' module:")
try:
    from modules.findMarkdown import extract_markdown_segments, process_transcripts_folder, handle_stream
    print("Module 'findMarkdown' imported successfully")
except ModuleNotFoundError as e:
    print(f"ModuleNotFoundError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

print("\nTrying to import 'messageColor' module:")
try:
    from modules.messageColor import some_function  # Replace `some_function` with the actual function you need
    print("Module 'messageColor' imported successfully")
except ModuleNotFoundError as e:
    print(f"ModuleNotFoundError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# Check if the system-message/clean_transcript/system.md file exists and read its content
system_message_path = os.path.join(script_dir, 'system-message', 'clean_transcript', 'system.md')
print(f"\nChecking if 'system.md' exists: {system_message_path}")
if os.path.isfile(system_message_path):
    print("'system.md' exists")
    try:
        with open(system_message_path, 'r') as file:
            system_message_content = file.read().strip()
        print("Successfully read 'system.md'")
        
        # Define the test message
        test_message = """all right welcome to unsupervised learning this is Daniel misler and today I'm super excited to announce a project I've been wanting to talk about for a very long time called substrate okay let's get into the project itself so what is it exactly that is really the question uh what substrate is is an open- Source framework for human understanding meaning and progress and you might be inclined to say what the hell does that mean and that it's a great question right so the purpose of the project is to make things that matter to humans more transparent discussable and ultimately because they're transparent and discussable they'll be more fixable so what kind of things are we talking about so we're calling these substrate components and these are the components of human meaning right when we talk about understanding meaning and progress these are the pieces that we're actually talking about so collections of things okay so the first thing is an idea collections of ideas a list of human novel ideas problems a list of our most important human problems our beliefs our models which are are ways of conceptualizing reality frames a list of narratives or lenses for perceiving reality a list of solutions that correspond to problems information sources so you'll have like New York Times uh the hill uh Breitbart uh lots of different sources of information government sources individual sources different media organizations it's got to be a comprehensive list and it's got to span different political ideologies that's really important here as we'll see later people so this is just individuals organizations of different types laws we're going to collect all different legislation starting with the US government but expanding out to pretty much the world at some point claims so this is a factual claim a truth Claim about the world votes a list of votes and results from laws that were submitted and voted on uh to basically say here's what um the votes were from different people so this is talking about Representatives voting on things right arguments a list of arguments that have been made uh in favor or against a particular thing funding sources lobbyists so a list of lobbyists in their agendas missions donations goals and facts so these are actually claims from up here but these are just verified ones and important to note that it could become true and then untrue again so you have to kind of keep this updated"""

        # Send a test message to the Ollama server
        print("\nSending a test message to the Ollama server:")
        system_message = {
            'role': 'system',
            'content': system_message_content
        }
        user_message = {
            'role': 'user',
            'content': test_message.strip()
        }
        messages = [system_message, user_message]
        response = ollama.chat(model='llama3.1:8b', messages=messages, stream=True)
        handle_stream(response)
    except Exception as e:
        print(f"An error occurred while reading 'system.md' or sending the test message: {e}")
else:
    print("'system.md' does not exist")