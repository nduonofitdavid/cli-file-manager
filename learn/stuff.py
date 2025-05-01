import os
import pathlib as ptl
from typing import Dict, List
import re
from datetime import datetime
import time


date_meta_data: Dict[str, List[int]] = {

}

file_meta_data: Dict[str, Dict[str, None]] = {

}

# os.scandir can be used to move in a directory, and get meta data about the files in that directory


for item in os.scandir():
    
    file_regex = r"^([a-zA-Z]+\d*)\.([a-zA-Z]{1,4})$"
    if(re.match(file_regex, item.name)):
        date = time.ctime(item.stat().st_ctime)
        size = item.stat().st_size
        date_readable = datetime.strptime(date, "%a %b %d %H:%M:%S %Y")

  #      print("size", size)
   #     print("date", date)
    #    print("date_readable", date_readable)

        try:
            date_meta_data[date_readable.year].append(date_readable.month)
        except:
            date_meta_data[date_readable.year] = [date_readable.month]
            
        # for keys in date_meta_data.keys():
        #     if not date_readable.year == keys:
        #         date_meta_data[date_readable.year] = [date_readable.month]
        #     else:
        #         date_meta_data[date_readable.year].append(date_readable.month)

# print(date_meta_data)

# the aim now is to rid the dictionary of duplicates



for key in date_meta_data.keys():
    copy = date_meta_data[key]
    clean_array = []
    item = copy[0]
    clean_array.append(item)
    for i in range(len(copy)):
        if not copy[i] == item:
            item = copy[i]
            clean_array.append(copy[i])


    date_meta_data[key] = clean_array

# print(date_meta_data)



def sort_by_size(directory):
    """
    Description: This function takes a directory, and sorts all the files in that directory
    based on their size

    Params:
        directory: str
    """
    os.chdir(directory)

    current_path = os.getcwd()

    os.mkdir("large")
    os.mkdir("medium")
    os.mkdir("small")

    for item in os.scandir():
        file_regex = r"^([a-zA-Z]+\d*)\.([a-zA-Z]{1,10})$"

        if(re.match(file_regex, item.name)):
            name = item.name
            size = item.stat().st_size

            category = ''

            if size < 1024:
                category = 'small'
            elif size > 1024 and size < 1048576:
                category = 'medium'
            else:
                category = 'large'
            destination = current_path + f'/{category}/{name}'
            source = current_path + f'/{name}'
            os.rename(source, destination)
            
        
        else:
            if item.name not in ('large', 'medium', 'small'):
                try:
                    os.chdir(item.name)
                    new_directory = os.getcwd()
                    sort_by_size(new_directory)
                except (NotADirectoryError, FileNotFoundError):
                    print(f"The item `{item}` is not a directory and a file also")

            
sort_by_size('/home/nduonofit/Projects/testdir')

# if the item is not a file, but is a folder, move into that directory, and then call the parent function again on that directory


# | Category | Range (approximate)         | Common Use Cases                                           |
# |----------|-----------------------------|------------------------------------------------------------|
# | **Small**  | 1 byte to ~1 KB             | Characters, flags, small messages, configuration files     |
# | **Medium** | ~1 KB to ~1 MB              | Text files, documents, images (e.g., PNG, JPEG)            |
# | **Large**  | ~1 MB to ~1 GB+             | Videos, databases, software packages, large datasets       |

# 1 Byte	8 bits
# 1 KB	1,024 bytes
# 1 MB	1,024 KB = 1,048,576 bytes
# 1 GB	1,024 MB = 1,073,741,824 bytes