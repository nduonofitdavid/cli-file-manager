import os
import time
from datetime import datetime

file_path = 'example.txt'

size = os.path.getsize(file_path) # get the size of the file in bytes
created = os.path.getctime(file_path) # get the time when the file was created
modified = os.path.getctime(file_path) # get the time when the file was recently modified



# with open('example.txt', 'w') as f:
#     for i in range(10 ** 7):
#         f.write(str(i))

# created returns values in timestamps,  we have to convert the timestamps into readable format

created_readable = time.ctime(created)
modified_readable = time.ctime(modified)

# print("Created: ", created_readable)
# print("Modified: ", modified_readable)
# print(created_readable == modified_readable)


created_data = datetime.strptime(created_readable, "%a %b %d %H:%M:%S %Y")
print(created_data)
print(created_data.day)
print(created_data.month)
print(created_data.year)