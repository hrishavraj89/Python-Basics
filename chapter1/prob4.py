import os

def print_directory_contents(path):
    for item in os.listdir(path):
        print(item)

# Replace 'your_directory_path' with the path of the directory you want to list
print_directory_contents('/')
