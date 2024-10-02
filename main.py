import os

#Stores directory to look into
directory_path = r"D:\Youtube.dra\MediaFiles\OG Library\Music"
#Stores the separator to use
separator = "\\"

music = []

def getFileName(file_path : str) -> str:
    dirs = file_path.split(separator)
    file = dirs[-1]
    #Omits last part of file extension
    return file[0:-4]

#Iterates through directories in file
def list_files_recursive(path='.'):
    for entry in os.listdir(path):
        full_path : str = os.path.join(path, entry)

        #Checks if path leads to a directory
        if os.path.isdir(full_path):
            list_files_recursive(full_path)
        elif "Music" in full_path:
            if "Kevin Macleod" in full_path:
                music.append(getFileName(full_path) + " - Kevin Macleod")
            else:
                music.append(getFileName(full_path))
        #Checks if path is in fact a file
        else:
            pass

# Specify the directory path you want to start from
# directory_path = input("Type in file path: ")
list_files_recursive(directory_path)
music = sorted(music)

for track in music:
    print(track)