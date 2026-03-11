import os
from functions.restrict_access_to_target_dir import restrict_access_to_target_dir

def get_files_info(working_directory: str, directory: str = "."):
    try:
        target_dir = restrict_access_to_target_dir(working_directory, directory)
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