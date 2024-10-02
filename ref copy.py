#Orignal link: https://www.geeksforgeeks.org/python-list-all-files-in-directory-and-subdirectories/
#https://www.geeksforgeeks.org/python-raw-strings/

import os

#Iterates through directoried in file
def list_files_recursive(path='.'):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)

        #Checks if path leads to a directory
        if os.path.isdir(full_path):
            list_files_recursive(full_path)
        #Checks if path is in fact a file
        else:
            print(full_path)

# Specify the directory path you want to start from
directory_path = './'
print(directory_path)
list_files_recursive(directory_path)