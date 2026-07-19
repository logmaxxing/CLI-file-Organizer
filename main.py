from pathlib import Path
import glob
# import json
from os import scandir, replace
from argparse import Namespace,ArgumentParser
import shutil

#parsers/args and variables
home = Path.home()

# You can add own extensions here under pre-defined folder names(Keys in file_types) 
# or Create your own separate one with this format, make sure you make it inside file_types disctionary
# "xyz":['.extentions']
file_types= {
    "Pictures" : [
        '.jpg','.png','.webp','.gif','.svg','.tiff','.tif','.heic','.heif','.bmp'
        ],
    "Videos" : [
        '.mp4','.mkv','.mov','.avi','.webm'
        ],
    "Audio" : [
        '.mp3','.wav','.m4a','.flac','.ogg'
    ],
    "Documents" : [
        '.pdf','.docx','.xlsx','.pptx','.txt','.csv'
    ],
    "dev_files" : [
        '.py','.js','.ts','.java','.cpp','.json','.md','.html','.css'
    ],
    "Packages" : [
        '.zip','.rar','.exe','.msi','.dmg','.pkg','.iso','.gz','.7z','.tar.bz2','.jar','.deb','.pacman','.sh','.tgz','.run','.bin','.desktop','.conf','.cfg','.zst'
    ]
}
'''
old way of me sorting files.
'''
# file_keys = file_types.keys()
# file_values = file_types.values()

EXT_MAP = {ext: category for category,exts in file_types.items() for ext in exts}
"""
Logic of EXT_MAP/extension_map -> dictionary Comprehension :

EXT_MAP = {}
for category,exts in file_types.items():
    for ext in exts:
        EXT_MAP[ext] = category

"""

def setup_args():
    """
    Arguments created here for the script.
    """
    
    parser = ArgumentParser()
    parser.add_argument("directory_path",help="Path of Directory[DON'T INCLUDE FROM HOME]",type=str)

    # adding mutualy exclusive parser for verbose and confirm
    task = parser.add_mutually_exclusive_group()
    task.add_argument('-v','--verbose',help='Shows the operations it will perform in the directory',action='store_true')
    task.add_argument('--confirm',help='performs oraginization actions',action='store_true')

    # same for file operation when a same file is found in both directories, parent and destination.
    method = parser.add_mutually_exclusive_group()
    method.add_argument('-s','--skip',help='skips operation for duplicate files.',action='store_true')
    method.add_argument('-o','--overwrite',help='Overwrites file in destination folder.',action='store_true')
    method.add_argument('-d','--delete',help='It deletes both same files from parent and destination directory',action='store_true')
    method.add_argument('-r','--remove',help='removes un-categorized files.',action='store_true')

    return parser.parse_args()

ARGS :Namespace = setup_args()
# vairable that stores directory_path value 'string'
full_path = Path(home/ARGS.directory_path)


# validates directory_path, whethere exists or not.
def verify_path(check_path)->bool:
    """checks whether the provided path by user exists or not."""
    
    try:
        if check_path.exists():
            return True
        else:
            return False
        return None
    except Exception as e:
        print(f"Error occured: {e}")
        return False
    return None

#fetching files in directory
def verbose_content()-> list:
    """
    Fetches files in all directory.
    """
    try:
        if verify_path(full_path):
            content = [
                dir.name for dir in Path.iterdir(full_path)
                if dir.is_file() and not dir.name.startswith(".")
            ]
            return content, f"{len(content)} files found."
        else:
            return f"No such Directory exists like : {full_path}"
    except Exception as e:
        return e
    return None

# checking whether sorting folders exists or not.
def check_folders():
    """
    Checks whether proper directories are present in the destination directory or not.
    if not then it creates it.
    """
    check_sum = {}
    try:
        if verify_path(full_path):
            for check in file_types.keys():
                check_sum[check] = Path(full_path/check).exists()
            folder_exists = all(check_sum.values())
            return check_sum, folder_exists
        else:
            return None, False
    except Exception as e:
        print(f"error checking folders: {e}")
    return None, False

# creating folder if False in check_folders()
def create_folders():
    """Creates the folders needed for sorting the directory content."""
    folders,store = check_folders()
    try:
        if verify_path(full_path):
            for key,value in folders.items():
                if folders[key] == True:
                    print(f"Folder found: {key}")
                    continue
                else:
                    Path(full_path/key).mkdir(exist_ok=True)
                    print(f"Folder created: {key}")
        return True
    except Exception as e:
        return False

# checking whether the files exist in the destination folder as well

def move_files():
    """function to Sort files acordingly."""
    # OLD way of sorting below:
    # for values in file_values:
    #     for files in verbose_content()[0]:
    #         if Path(full_path/files).suffix in values:
    #             print(f"{files} exists in {values}")
    #             way = [key for key in file_keys if file_types[key] == values]
    #             shutil.move(full_path/files,full_path/way[0])
    try:
        # optimized and improved way:
        files,_ = verbose_content()

        # checking if directory even has files.
        if not files:
            print("No files to organize.")
            return 
        

        for file_name in files:
            #full path of each file
            file_path = full_path/file_name 

 
            suffix = file_path.suffix.lower()

            if suffix in EXT_MAP:
                dest_folder = full_path/EXT_MAP[suffix]
                #full path to chech if files exist in destination folder.
                dest_file_path = full_path/dest_folder/file_name 

                # ---------VERBOSE---------#
                if ARGS.verbose:
                    print(f"[PREVIEW] Moving {file_name} -> {dest_folder}")

                # ---- CONFIRMATION----#
                elif ARGS.confirm:
                 # ----Duplication check-----#
                    if dest_file_path.exists():

                        if ARGS.skip:
                            print(f"[SKIPPED] Duplicate Found: {file_name}")
                            continue
                        elif ARGS.overwrite:
                            print(f"[OVERWRITE] Replacing : {file_name}")
                            shutil.copy2(file_path,dest_folder)
                            Path(file_path).unlink()
                        elif ARGS.delete:
                            file_path.unlink()
                            dest_file_path.unlink()
                            print(f"[DELETED] {file_name} from Both Directories")
                            continue
                        else:
                            print(f"[SKIPPED] {file_name} exists (No conflict flag set).")
                    else:
                        print(f"[MOVED] {file_name} -> {dest_folder}")
                        shutil.move(file_path,dest_folder)
            else:
                if ARGS.remove:
                    if file_path.suffix not in EXT_MAP:
                        file_path.unlink()
                        print(f"[REMOVED] {file_name} -> not categorized.")
                else:
                    print(f"[SKIPPED] {file_name} not categorized.")
        return True
    except Exception as e:
        return False


def execute():
    """Main Execution of the script."""
    if not verify_path(full_path):
        print(f"Directory -> {full_path.name} doesn't exist at {full_path}.")
        return
        
    folder_map, state = check_folders()
    if state is False:
        print(f"{full_path.name} exists.")
        # print("i think they don't") -> for testing, pre-alpha script
        print("Sorting folders are Missing.")
        print("Creating now... ")
        create_folders()
        print("\nAll Folders created Successfully.\n")
        move_files()
    else:
        print("Executing sorting process now...")
        success = move_files() 
        if success:
            print("\nSorting Completed Sucessfully!")
        else:
            print("\nSorting process finished with Warnings or no files moved.")
if __name__ == "__main__":
    execute()
