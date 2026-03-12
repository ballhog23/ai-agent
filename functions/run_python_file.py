import os
import subprocess
from google import genai
from google.genai import types

def run_python_file(working_directory: str, file_path: str, args: None | list =None):
    try:
        working_dir_abs: str = os.path.abspath(working_directory)
        target_file: str = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # determine if target directory is within working dir abs path
        valid_target_dir: bool = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # splitext returns (root, ext) tuple, ext could be empty
        root, extension = os.path.splitext(target_file)
        if not extension == '.py':
            return f'Error: "{file_path}" is not a Python file'

        # building command to run in a subprocess
        command = ["python", target_file]

        if args:
            command.extend(args)
        
        result = subprocess.run(args=command, text=True, capture_output=True, timeout=30, cwd=working_dir_abs)

        return build_return_string(result.returncode, result.stdout, result.stderr)
        
    except Exception as e:
        return f"Error: executing Python file: {e}"

def build_return_string(exit_code: int, std_out: str | None, std_err: str | None) -> str:
    output_str_list = []

    if exit_code != 0:
        output_str_list.append(f"Process exited with code {exit_code}")
    
    if not std_out and not std_err:
        output_str_list.append("No output produced")

    if std_out:
        output_str_list.append(f"STDOUT:\n{std_out}")

    if std_err:
        output_str_list.append(f"STDERR:\n{std_err}")

    return "\n".join(output_str_list)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file in a specified directory relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the file to execute, relative to the working directory (default is the working directory itself)",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="A list of string arguments to pass to the function upon invocation",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="The string argument to pass to the function upon invocation",
                )       
            ),
        },
    ),
)