import os
from typing import List
import json

def sort_by_size(directory: str, subdirectory:str = None) -> bool:
    """
    Description: This function takes a directory and then sorts all the items in that directory
    based on size.

    Params:
        directory: str
    
    Returns:
        bool -> In order to indicate if the operation was successful or not
    """

    actions: List[dict] = []
    
    # base_dir = os.getcwd()
    # seperator = os.sep # it is better to make use of os.path.join when joining files together, this is a more
    # modern approach and makes it more readable and easy to use.

    main_dir = os.getcwd()
    base_dir = directory
    current_dir = subdirectory if subdirectory else base_dir


    for folder in ['cli_sort_small', 'cli_sort_medium', 'cli_sort_large']:
        os.makedirs(os.path.join(current_dir, folder), exist_ok=True)



    small_destination = os.path.join(current_dir, 'cli_sort_small')
    medium_destination = os.path.join(current_dir, 'cli_sort_medium')
    large_destination = os.path.join(current_dir, 'cli_sort_large')

    try:
        for entry in os.scandir(current_dir):

            if entry.name.startswith('cli_sort_'):
                return

            if entry.is_file():
                file_size = entry.stat().st_size
                source = entry.path
        
                if file_size  < 10_240:
                    destination = os.path.join(small_destination, entry.name)

                elif file_size < 1_048_576:
                    destination = os.path.join(medium_destination, entry.name)

                else:
                    destination = os.path.join(large_destination, entry.name)

                os.rename(source, destination)
                actions.append({"action": f"mv {source} {destination}"})

            elif entry.is_dir():
                actions.append({"action": f"cd {entry.path}"})
                sort_by_size(base_dir, entry.path)

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
    
if __name__ == "__main__":
    sort_by_size(r'C:\Users\WALEX BIZ GROUP\Documents\David\seventeenthmarch\pypractice\sortme')