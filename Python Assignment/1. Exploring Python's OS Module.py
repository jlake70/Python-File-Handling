

import os

def list_directory_contents(filename):
    try:
        items = os.listdir(filename)
        print(f" Contents in the file: {filename}")
        for item in items:
            item_path = os.path.join(filename, item)
            if os.path.isdir(item_path):
                print(f"Directory: {item}")
            else:
                print(f"File: {item}")
    except FileNotFoundError:
        print(f"{filename} not found.")
    except PermissionError:
        print(f"Permission to access {filename} is not permitted.")
    except Exception as e:
        print(f"Unexpected error: {e}")

directory_path = input("Enter the directory path: ")
    

list_directory_contents(directory_path)