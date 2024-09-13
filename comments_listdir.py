# import os module
import os

# specify directory path
directory_path = "C:\\"
# listdir Function

try:
    # os.listdir to list the item
    content = os.listdir(directory_path)
    print(f"Content of '{directory_path}'")

    # use for loop to print the list of content in each file
    for item in content:
        print(item)
        # if file does not exist
except FileNotFoundError:
    print(f"The directory {directory_path} does not exist")