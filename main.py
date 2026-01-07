import os

#Stores directory to look into
directory_path = r""

#Stores the separator to use
separator = "\\"

sites_to_credit = [
    "vecteezy"
]

#Tracks that may or may not be in the video:
possible_tracks = [
    "Atlantis - AudioNautix",
    "Accepting Defeat - Experia",
    "Carless Whisper",
    "Come Thru",
    "Danganronpa Mauve Pre Trial",
    "Drop - Anno Domini Beats",
    "Exhilarate",
    "Jeopardy Theme",
    "Tech diff Music"
]

kevin_macleod_cred = """by Kevin MacLeod (incompetech.com)
Licensed under Creative Commons: By Attribution 4.0 License
http://creativecommons.org/licenses/by/4.0/"""

clips = []
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

            #If track exists in list fo expected tracks, skip
            if getFileName(full_path) in possible_tracks:
                continue
            #f track comes from kevin Macleod folder, provide credit
            elif "Kevin Macleod" in full_path:
                music.append(getFileName(full_path) + " - Kevin Macleod\n" + kevin_macleod_cred)
            #Otehrwise, just add it to list
            else:
                music.append(getFileName(full_path))
        #If video comes from CLIPS
        elif "Clips" in full_path:
            for site in sites_to_credit:
                if site in full_path and not(site in clips):
                    clips.append(site + " - " +  str(getFileName(full_path)))
        #Does nothing else if cases above aren't met
        else:
            pass

# Specify the directory path you want to start from
# directory_path = input("Type in file path: ")

list_files_recursive(directory_path)

#Sorts the final array alphabetically
music = sorted(music)

#Includes other credit to give (from CLIPS)
print("These are some sites to give credit to")
for clip in clips:
    print("O " + clip)
print()

#Prints list of possible track used
if possible_tracks.count != 0:
    print("These are the possible tracks that MAY or may not not be in video:")
    for track in possible_tracks:
        print("O " +  track)
    print()

if music.count != 0:
    print("These are the tracks that are DEFINITELY in the video:")
    #Prints each one individually
    for track in music:
        print("O " + track)
