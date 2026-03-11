import os
from config import MAX_CHARS

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