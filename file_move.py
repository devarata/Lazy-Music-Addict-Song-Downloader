import os
import shutil
import glob

def moving():
    list_of_files = glob.glob('C:\\Users\\devar\\Downloads\\*')
    latest_file = max(list_of_files, key=os.path.getctime)
    latest_file = latest_file.replace('\\','\\\\')
    filename = latest_file.strip().split("\\")
    filename = filename[len(filename)-1]
    print(filename)
    #change according to your convenience
    #destination="C:\\Users\\devar\\Desktop\\MyDownloadedSongs"
    destination="C:\\Users\\devar\\Music\\Playlists"
    if not os.path.exists(destination):
        os.makedirs(destination)

    destination=destination+"\\"+filename
    print(destination)


    os.rename(latest_file,destination)
