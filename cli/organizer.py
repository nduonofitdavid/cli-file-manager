from typing import List
import os
import re
import json
from datetime import datetime


def sort_by_extension(base_dir: str, subdirectory: str | None = None) -> bool:
    """
    Description: Function to move files into their respective folders based on extensions
    Params:
        base_dir: str
        subdirectory: str | None = None
    Returns:
        bool -> This signifies if the operation was completed or not
    """

    actions: List[dict] = []
    current_dir = subdirectory if subdirectory else base_dir
    main_dir = os.getcwd()

    try:
        for entry in os.scandir(current_dir):
            if entry.is_file():
                file_name = entry.name
                file_extension_regex = r"^([\w\-]+(?:\.[\w\-]+)*)\.([a-zA-Z0-9]{1,12})$"
                match = re.match(file_extension_regex, file_name)
                if match:
                    _, file_ext = match.groups()
                    print("File ext", file_ext)
                    os.makedirs(os.path.join(current_dir, "cli_app_" + file_ext), exist_ok=True)
                    ext_folder = os.path.join(current_dir, "cli_app_" + file_ext)
                    destination = os.path.join(ext_folder, file_name)
                    source = entry.path
                    os.rename(source, destination)
                    actions.append({"action": f"mv {source} {destination}"})
            elif entry.is_dir():
                actions.append({"action": f"cd {entry.path}"})
                sort_by_extension(base_dir, entry.path)
                
        log_dir = os.path.join(main_dir, "logs")
        os.makedirs(log_dir, exist_ok=True)
        logpath = os.path.join(log_dir, "logfile.jsonl")


        with open(logpath, "a") as f:
            for value in actions:
                f.write(json.dumps(value) + "\n")

        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    


def sort_by_size(directory: str, subdirectory: str | None = None) -> bool:
    """
    Sort files by size in a directory and its subdirectories.

    Params:
        directory: str - Root directory to start sorting
        subdirectory: str - Used for recursive sorting
    Returns:
        bool - Indicates if operation was successful
    """

    actions: List[dict] = []

    base_dir = directory
    current_dir = subdirectory if subdirectory else base_dir
    main_dir = os.getcwd()  

    # Create sorting folders in current directory
    for folder in ['cli_sort_small', 'cli_sort_medium', 'cli_sort_large']:
        os.makedirs(os.path.join(current_dir, folder), exist_ok=True)

    small_destination = os.path.join(current_dir, 'cli_sort_small')
    medium_destination = os.path.join(current_dir, 'cli_sort_medium')
    large_destination = os.path.join(current_dir, 'cli_sort_large')

    try:
        for entry in os.scandir(current_dir):
            # Skip the sorting folders
            if entry.name.startswith("cli_sort_"):
                continue

            if entry.is_file():
                file_size = entry.stat().st_size
                source = entry.path

                if file_size < 10_240:
                    destination = os.path.join(small_destination, entry.name)
                elif file_size < 1_048_576:
                    destination = os.path.join(medium_destination, entry.name)
                else:
                    destination = os.path.join(large_destination, entry.name)

                os.rename(source, destination)
                actions.append({"action": f"mv {source} {destination}"})

            elif entry.is_dir():
                actions.append({"action": f"cd {entry.path}"})
                sort_by_size(base_dir, entry.path)  # Recurse

        # Ensure logs directory exists
        log_dir = os.path.join(main_dir, "logs")
        os.makedirs(log_dir, exist_ok=True)
        logpath = os.path.join(log_dir, "logfile.jsonl")

        with open(logpath, "a") as f:
            for value in actions:
                f.write(json.dumps(value) + "\n")

        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def sort_by_date(directory: str, subdirectory: str | None = None) -> bool:
    """
    Sort files by size in a directory and its subdirectories.

    Params:
        directory: str - Root directory to start sorting
        subdirectory: str - Used for recursive sorting
    Returns:
        bool - Indicates if operation was successful
    """

    actions: List[dict] = []

    base_dir = directory
    current_dir = subdirectory if subdirectory else base_dir 
    main_dir = os.getcwd()

    try:
        for entry in os.scandir(current_dir):
            if entry.is_file():
                file = entry
                source = file.path
                creation_date = datetime.fromtimestamp(file.stat().st_ctime)
                year = os.path.join(current_dir, str(creation_date.year))
                month_n_day = f"{creation_date.month}-{creation_date.day}"
                print(year, month_n_day)
                os.makedirs(year, exist_ok=True)
                month_n_day_dir_name = os.path.join(year, month_n_day)
                os.makedirs(month_n_day_dir_name, exist_ok=True)
                destination = os.path.join(month_n_day_dir_name, file.name)
                os.rename(source, destination)
                actions.append({"action": f"mv {source} to {destination}"})
        
            elif entry.is_dir():
                actions.append({"action": f"cd {entry.path}"})
                sort_by_date(entry.path)
        
        log_dir = os.path.join(main_dir, "logs")
        os.makedirs(log_dir, exist_ok=True)
        logpath = os.path.join(log_dir, "logfile.jsonl")

        with open(logpath, 'a') as logbook:
            for action in actions:
                logbook.write(json.dumps(action))
                
        return True
    except Exception as e:
        print(f"Something went wrong {e}")
        return False

        

if __name__ == "__main__":
    sort_by_date('test_folder')
