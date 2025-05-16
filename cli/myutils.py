from typing import List
import re
import os
import json

def get_extensions(folder: List[str]) -> List[str]:
    
    """
    Description: Returns a list containing all the extension names of the files in a directory
    Params: 
        folder: List[str]
    """

    extensions: List[str] = []
    extension_regex = r"^([a-zA-Z]+\d*)\.([a-zA-Z]{1,4})$"
    for file in folder:
        match = re.match(extension_regex, file)
        if match:
            _, file_ext = match.groups()
            if file_ext not in extensions:
                extensions.append(file_ext)
    return extensions


# def json_helper(path: str) -> bool:
#     try:

#         with open(path, "r") as f:
#             logs = [json.loads(line) for line in f if line.strip()]
        
       
#         with open(path, "w") as f:
#             json.dump(logs, f, indent=4)

#         return True

#     except (FileNotFoundError, json.JSONDecodeError) as e:
#         print(f"Error: {e}")
#         return False


def make_folders(folders: List[str], dir: str) -> bool:
    """
    Description: This function makes the folders in which the files will be be stored in and also
        logs the operation to a json file
    Params: 
        folders: List[str]
        dir: str
    Return: bool
    """
    base_dir = os.getcwd()
    log_entry = {

    }
    try:
        os.chdir(dir) # move into the users directory
    except NotADirectoryError:
        return False
    
    newdir = os.getcwd()

    for names in folders:
        os.mkdir(names)
    seperator = os.sep

    for i in range(len(folders)):
        log_entry[i] = f"mkdir {newdir}{seperator}{folders[i]}"
    
    os.chdir(base_dir)

    logpath = f"{base_dir}{seperator}logs{seperator}logfile.jsonl"

    with open(logpath, "a") as f:
        for value in log_entry.values():
            f.write(json.dumps({"action": value}) + "\n")

    # json_helper(logpath)
    return True
    


    # ext_regex = r"^([a-zA-Z]+\d*)\.([a-zA-Z]{1,4})$"
    # match = re.match(ext_regex, file)

    # if match:
    #     file_name, file_ext = match.groups() # tuple unpacking.
    #     print(file_ext)


play_folder = [
    'app.txt',
    'app.txt',
    'app.txt',
    'app.txt',
    'app.txt',
    'app.txt',
    'app.txt',
]


# print(get_extensions(play_folder))
        




# def get_extensions(folder: List[str]) -> List[str]:
#     extensions: List[str] = []
#     extension_regex = r"\.([A-Za-z0-9]{1,5})$"
    
#     for file in folder:
#         _, ext = os.path.splitext(file)  # split filename and extension
#         match = re.match(extension_regex, ext)
#         if match:
#             extensions.append(match.group(1))  # use .group(1) to get the extension string
#     return extensions

# play_folder = [
#     'app.txt',
#     'image.jpeg',
#     'script.py',
#     'README',
#     'archive.tar.gz',
#     'video.mp4',
#     'song.m4a',
#     'song.m4a'
# ]

# print(get_extensions(play_folder))












