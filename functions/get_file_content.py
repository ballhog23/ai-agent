import os
from config import MAX_CHARS
from google import genai
from google.genai import types

def get_file_content(working_directory: str, file_path: str):
    try:
        working_dir_abs: str = os.path.abspath(working_directory)
        target_file: str = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # determine if target directory is within working dir abs path
        valid_target_dir: bool = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_dir:
            f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            f'Error: File not found or is not a regular file: "{file_path}"'
        
        return read_file(target_file)

    except Exception as e:
        return f"Error reading file content: {e}"

def read_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        file_contents = file.read(MAX_CHARS)

        if file.read(1):
            file_contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
    return file_contents

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a file in a specified directory relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the file to read the contents of, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)