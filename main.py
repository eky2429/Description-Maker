import os

music = []


def getFileName(file_path : str) -> str:
    #Find index of last /
    slash_index = 0
    for i in range(-1, -len(file_path) - 1):
        if file_path[i] == "/":
            slash_index = len(file_path) - i

    #Find index of last .
    dot_index = 0
    for i in range(-1, -len(file_path) - 1):
        if file_path[i] == ".":
            slash_index = len(file_path) - i

    #find index of last
    return file_path[slash_index + 1:dot_index]

#Iterates through directories in file
def list_files_recursive(path='.'):
    for entry in os.listdir(path):
        full_path : str = os.path.join(path, entry)

        #Checks if path leads to a directory
        if os.path.isdir(full_path):
            list_files_recursive(full_path)
        elif full_path.endswith(".mp3"):
            if "Kevin Macleod" in full_path:
                music.append("Kevin Macleod - " + getFileName(full_path))
            else:
                music.append(getFileName(full_path))
        #Checks if path is in fact a file
        else:
            pass

# Specify the directory path you want to start from
directory_path = './'
directory_path = input("Type in file path: ")
list_files_recursive(directory_path)