'''
    Things to consider:
        i) This is Script I
        ii) The game should be set on English Language first (change this in game or launcher settings)
        iii) After copying these files (running this script), change the language to Japanese in game settings
        iv) Run the Script II, and check instructions in there
        v) If you want to change languages other than English and Japanese, watch videos online and replace the file names accordingly (marked with #*)
        vi) Also check if your game is in C drive, if elsewhere, change the C:\ on file names (marked with #*) or reinstall game on C
        vii) This needs to be done on every game update because it replaces the audio and text with the one you set on (a type of self-fix because this is modified), so I made this script to save some minutes :D (if the game has Japanese text and Audio, then redo from Script I)
        viii) Most important part, install Python before doing this. I should have put this point at the top because its so important but too lazy to reconfigure the numbers
'''

import shutil
import os

def copy_files_to_folder(file_paths, destination_folder):
    try:
        # Create the destination folder if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Copy each file to the destination folder
        shutil.copy(file_paths[0], os.path.join(destination_folder, 'ja_JP_Text-WindowsClient.pak')) #*
        
        shutil.copy(file_paths[1], os.path.join(destination_folder, 'ja_JP_Text-WindowsClient.sig')) #*
        
        print(f"File '{file_paths[0], file_paths[1]}' copied to '{destination_folder}' successfully.")

        print("Files copied and renamed successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace these with your actual file names and destination folder path
    TextPAK = 'C:\Riot Games\VALORANT\live\ShooterGame\Content\Paks\en_US_Text-WindowsClient.pak' #*
    TextSIG = 'C:\Riot Games\VALORANT\live\ShooterGame\Content\Paks\en_US_Text-WindowsClient.sig' #*
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    destination_folder = documents_path + '\Valorant Text Packs' #*

    # List of file paths to copy
    files_to_copy = [TextPAK, TextSIG]

    # Call the function to copy files to the destination folder
    copy_files_to_folder(files_to_copy, destination_folder)