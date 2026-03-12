import os
from google import genai
from google.genai import types

def write_file(working_directory: str, file_path: str, content: str):
    try:
        working_dir_abs: str = os.path.abspath(working_directory)
        target: str = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # determine if target directory is within working dir abs path
        valid_target_dir: bool = os.path.commonpath([working_dir_abs, target]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            
        if os.path.isdir(target):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        # create parent directories if not exist
        parent_dirs = os.path.dirname(target)
        os.makedirs(parent_dirs, exist_ok=True)

        return write_to_file(target, content)

    except Exception as e:
        return f"Error writing to file: {e}"
    
def write_to_file(file_path: str, content: str) -> str:
    with open(file_path, "w") as file:
        file.write(content)
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to a file in a specified directory relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the file to write to, relative to the working directory (default is the working directory itself)",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The string content to write to the file",
            ),
        },
    ),
)