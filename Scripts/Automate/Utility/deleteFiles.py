import os
import shutil

def delete_files_in_folder(folder_path):
    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            print(f"Error: The folder {folder_path} does not exist.")
            return
        
        # Loop through all the files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            try:
                # Check if it's a file before deleting
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                # If it's a directory, remove it
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print(f"Deleted folder: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

    except Exception as e:
        print(f"Error accessing the folder {folder_path}: {e}")

# List of folders to delete files from
folders = [
    r"C:\Users\rastr\Downloads\InputImages",
    r"C:\Users\rastr\Downloads\RemovedBG",
    r"C:\Users\rastr\Downloads\ProcessedImages"
]

# Iterate through the folders and delete files
for folder in folders:
    delete_files_in_folder(folder)