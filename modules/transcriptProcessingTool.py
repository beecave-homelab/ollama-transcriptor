from gradio_tools import GradioTool
from modules.transcriptProcessor import check_file_type, read_file_content, process_content
from typing import Any, Tuple, List

class TranscriptProcessingTool(GradioTool):
    """Tool for processing uploaded transcript files"""

    def __init__(self, name="TranscriptProcessor", description="A tool to process uploaded transcript files.", src="$HOME/Nextcloud/Projects/ollama-transcriptor"):
        super().__init__(name, description, src)

    def create_job(self, file_path: str) -> List[str]:
        if check_file_type(file_path):
            content = read_file_content(file_path)
            return process_content(content)
        else:
            raise ValueError("Unsupported file type. Only .txt and .md files are supported.")

    def postprocess(self, output: Tuple[Any] | Any) -> str:
        return '\n---\n'.join(output)

    def _block_input(self, gr) -> "gr.components.Component":
        return gr.File()

    def _block_output(self, gr) -> "gr.components.Component":
        return gr.Textbox()


# from gradio_tools import GradioTool
# from modules.transcriptProcessor import check_file_type, read_file_content, process_content
# import os
# from typing import Any, Tuple, List

# class TranscriptProcessingTool(GradioTool):
#     """Tool for processing uploaded transcript files"""

#     def __init__(
#         self,
#         name="TranscriptProcessor",
#         description=(
#             "A tool to process uploaded transcript files. Use this to check if the content "
#             "has more than 1000 words, split the content into segments of 1000 words or less, "
#             "and send it to the chatbot for processing."
#         ),
#         src="path/to/your/gradio/space",
#         hf_token=None,
#     ) -> None:
#         super().__init__(name, description, src, hf_token)

#     def create_job(self, file_path: str) -> List[str]:
#         if check_file_type(file_path):
#             content = read_file_content(file_path)
#             return process_content(content)
#         else:
#             raise ValueError("Unsupported file type. Only .txt and .md files are supported.")

#     def postprocess(self, output: List[str]) -> str:
#         return '\n---\n'.join(output)

#     def _block_input(self, gr) -> "gr.components.Component":
#         return gr.File()

#     def _block_output(self, gr) -> "gr.components.Component":
#         return gr.Textbox()
    
#     def handle_segments(self, segments: List[str]):
#         for segment in segments:
#             yield segment