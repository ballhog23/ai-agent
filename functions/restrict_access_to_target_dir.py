import os

def restrict_access_to_target_dir(working_directory: str, directory: str = "."):
    working_dir_abs: str = os.path.abspath(working_directory)
    target_dir: str = os.path.normpath(os.path.join(working_dir_abs, directory))
    # determine if target directory is within working dir abs path
    valid_target_dir: bool = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    return target_dir