
import os
directory_path = "E:\\"
# listdir Function
try:
    content = os.listdir(directory_path)
    print(f"Content of '{directory_path}'")
    for item in content:
        print(item)
except FileNotFoundError:
    print(f"The directory {directory_path} does not exist")