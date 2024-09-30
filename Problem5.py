import os

# Prints th contents in the directory
def print_directory_contents(path):
    try:
        entries = os.listdir(path)
        for entry in entries:
            print(entry)
    except Exception as e:
        print(e)

print_directory_contents('.')
