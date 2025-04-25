from typing import List
import os
import re


def sort_by_folder(folder: List[str], base_dir: str) -> bool:
    """
    Description: Function to move files into their respective folders based on extensions
    Params:
        folder: List[str]
        base_dir: str
    Returns:
        bool
    """
    extension_regex = r"^([a-zA-Z]+\d*)\.([a-zA-Z]{1,4})$"
    
    for file in folder:
        match = re.match(extension_regex, file)
        if match:
            file_name, file_ext = match.groups()
            destination = base_dir + f'/{file_ext}/{file_name}.{file_ext}'
            source = base_dir + f'/{file_name}.{file_ext}'
            os.rename(source, destination)

