import os

def print_directory_contents(path):
    try:
        # List all entries in the directory given by 'path'
        entries = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")

# Example usage
directory_path = '.'  # Current directory
print_directory_contents(directory_path)
