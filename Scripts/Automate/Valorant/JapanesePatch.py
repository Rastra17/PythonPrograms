'''
    Things to consider:
        i) This is Script II
        ii) Run Script I before doing this or you may encounter a fatal error
        iii) If haven't, change in-game language to Japanese after running Script I
        iv) Run this script, it will replace Japanese text with English text while the Audio remains Japanese
        v) Enjoy your modified game :)
        vi) ~ If you want to change languages other than English and Japanese, watch videos online and replace the file names accordingly (marked with #*)
        vii) ~ Also check if your game is in C drive, if elsewhere, change the C:\ on file names (marked with #*) or reinstall game on C
        viii) ~ This needs to be done on every game update because it replaces the audio and text with the one you set on (a type of self-fix because this is modified), so I made this script to save some minutes :D (if the game has Japanese text and Audio, then redo from Script I)
'''

import os
import shutil

def replace_files(source_folder, old_files, destination_folder, new_files):
    try:
        # Delete old files from the destination folder
        for old_file in old_files:
            old_file_path = os.path.join(destination_folder, old_file)
            if os.path.exists(old_file_path):
                os.remove(old_file_path)
                print(f"Old file '{old_file}' deleted from '{destination_folder}'.")
            else:
                print("No old files exists")

        # Copy new files to the destination folder
        for i in range(len(new_files)):
            new_file_path = os.path.join(source_folder, new_files[i])
            destination_file_path = os.path.join(destination_folder, new_files[i])
            shutil.copy(new_file_path, destination_file_path)
            print(f"New file '{new_files[i]}' copied to '{destination_folder}' successfully.")

        print("Files replaced successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace these with your actual file names and folder paths
    source_folder_path = os.path.join(os.path.expanduser("~"), "Documents") + '\Valorant Text Packs'
    old_files_to_delete = ['ja_JP_Text-WindowsClient.pak', 'ja_JP_Text-WindowsClient.sig'] #*
    destination_folder_path = 'C:\Riot Games\VALORANT\live\ShooterGame\Content\Paks' #*
    new_files_to_copy = old_files_to_delete

    # Call the function to replace files in the destination folder
    replace_files(source_folder_path, old_files_to_delete, destination_folder_path, new_files_to_copy)