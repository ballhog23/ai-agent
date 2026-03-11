import os

def get_files_info(working_directory: str, directory: str = "."):
    try:
        working_dir_abs: str = os.path.abspath(working_directory)
        target_dir: str = os.path.normpath(os.path.join(working_dir_abs, directory))
        # determine if target directory is within working dir abs path
        valid_target_dir: bool = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        dir_contents_list = os.listdir(target_dir)

        return get_dir_contents_info(dir_contents_list, target_dir)
    
    except Exception as e:
        return f"Error listing files: {e}"

def get_dir_contents_info(contents: list[str], target_dir: str):
    content_data_list: list[str] = []

    for content in contents:
        path_to_content: str = os.path.join(target_dir, content)
        is_dir = os.path.isdir(path_to_content)
        file_size = os.path.getsize(path_to_content)
        content_data_list.append(f"- {content}: file_size={file_size} bytes, is_dir={is_dir}")

    return "\n".join(content_data_list)