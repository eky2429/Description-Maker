import os

#Stores directory to look into
directory_path = r"D:\Youtube.dra\MediaFiles\OG Library\Music"
#Stores the separator to use
separator = "\\"

music = []

def getFileName(file_path : str) -> str:
    #Obtains the file name alone
    dirs = file_path.split(separator)
    file = dirs[-1]
    #Omits file extension of file
    return file[0:-4]

#Iterates through directories in file
def list_files_recursive(path='.'):
    for entry in os.listdir(path):
        full_path : str = os.path.join(path, entry)

        #Calls function again on updated path
        if os.path.isdir(full_path):
            list_files_recursive(full_path)
        #Checks if file is inside a "Music" directory
        elif "Music" in full_path:
            if "Kevin Macleod" in full_path:
                music.append(getFileName(full_path) + " - Kevin Macleod")
            else:
                music.append(getFileName(full_path))
        #Does nothing else if cases above aren't met
        else:
            pass

# Specify the directory path you want to start from
# directory_path = input("Type in file path: ")

list_files_recursive(directory_path)
#Sorts the final array alphabetically
music = sorted(music)

#Prints each one individually
for track in music:
    print(track)