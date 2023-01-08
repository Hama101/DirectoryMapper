from config import *
import os
import time
from typing import (
    List,
    Tuple,
)
import re


# Function to list all files and directories in the given directory
@safe_call
def list_files(dir : str) -> List[str]:
    return os.listdir(dir)

# Function to get only the files from the given directory list
@safe_call
def get_files(dir : str) -> Tuple[str]:
    lst : List[str] = [file for file in list_files(dir) if os.path.isfile(os.path.join(dir, file))]
    return tuple(lst)

@safe_call
def move_file(file_path : str) -> None:
    file_extension : str = os.path.splitext(file_path)[1].replace(".", "")
    if file_extension in ZIP_EXTENSTIONS:
        dest_dir = ZIP_DIR
    elif file_extension in IMAGE_EXTENSTIONS:
        dest_dir = IMAGES_DIR
    elif file_extension in VIDEO_EXTENSTIONS:
        dest_dir = VIDEOS_DIR
    elif file_extension in AUDIO_EXTENSTIONS:
        dest_dir = AUDIO_DIR
    elif file_extension in EXE_EXTENSTIONS:
        dest_dir = EXE_DIR
    elif file_extension in PDF_EXTENSTIONS:
        dest_dir = PDF_DIR
    elif file_extension in XLXS_EXTENSTIONS:
        dest_dir = XLXS_DIR
    elif file_extension in DOC_EXTENSTIONS:
        dest_dir = DOC_DIR
    elif file_extension in JSON_EXTENSTIONS:
        dest_dir = JSON_DIR
    else:
        dest_dir = OTHERS_DIR
    
    print(dest_dir)
    # move the file now
    print(f"\033[92mMoving {file_path} to {dest_dir}\033[0m")
    try:
        os.rename(file_path, os.path.join(dest_dir, os.path.basename(file_path)))
    except Exception as e:
        print(f"\033[91m{e}\033[0m")
    print(f"\033[92mMoved.\033[0m")


# remove duplicates files from the main directory
@safe_call
def remove_duplicates(lst : List[str]) -> List[str]:
    # duplicate files have copy or (number) in their name
    # so we will remove them
    # we will use regex to find the duplicate files
    # and then remove them
    
    duplicates : List[str] = []
    for file in lst:
        if re.search(r'copy', file, re.IGNORECASE) or re.search(r'\(\d+\)', file):
            duplicates.append(file)

    for file in duplicates:
        lst.remove(file)
        # use os.remove to remove the file
        print(f"\033[92mRemoving {file}\033[0m")
        os.remove(os.path.join(DOWNLOADS_DIR, file))
        print(f"\033[92mRemoved.\033[0m")
    return lst



def main() -> None:
    while True:
        # get the files list
        files_list : Tuple[str] = get_files(DOWNLOADS_DIR)

        # if not len(files_list):
        #     # print red message
        #     print(f"\033[91mNo files to move.\033[0m")
        #     break

        print(f"\033[92mRemoving duplicates...\033[0m")
        # remove duplicates
        files_list = remove_duplicates(list(files_list))
        print(f"\033[92mRemoved.\033[0m")
        print(f"\033[92mMoving files...\033[0m")
        
        # move files
        for file in files_list:
            move_file(os.path.join(DOWNLOADS_DIR, file))
        print(f"\033[92mMoved.\033[0m")
        print(f"\033[92mSleeping for {SLEEP_TIME} seconds...\033[0m")
        
        # sleep 
        time.sleep(SLEEP_TIME)

        

if __name__ == "__main__":
    main()