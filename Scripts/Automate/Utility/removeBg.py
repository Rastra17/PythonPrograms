import os
import cv2
from rembg import remove

# Get the user's home directory and Downloads folder
home_directory = os.path.expanduser('~')
downloads_folder = os.path.join(home_directory, 'Downloads')

# Create the 'InputImages' folder inside Downloads for input images
InputImages_folder = os.path.join(downloads_folder, 'InputImages')
os.makedirs(InputImages_folder, exist_ok=True)  # Create folder if it doesn't exist

# Create the 'RemovedBG' folder inside Downloads for output images
removedbg_folder = os.path.join(downloads_folder, 'RemovedBG')
os.makedirs(removedbg_folder, exist_ok=True)  # Create folder if it doesn't exist

# Allowed image file extensions
allowed_extensions = ['.jpg', '.jpeg', '.png']

# Process every image in the 'InputImages' folder
for file in os.listdir(InputImages_folder):
    file_path = os.path.join(InputImages_folder, file)
    
    # Check if the file is an image with an allowed extension
    if os.path.isfile(file_path) and os.path.splitext(file)[1].lower() in allowed_extensions:
        print(f"Processing: {file}")

        # Read the input image
        input_image = cv2.imread(file_path)

        # Remove the background
        output_image = remove(input_image, bgcolor= (255, 255, 255, 255))

        # Save the output image in the 'RemovedBG' folder with the same filename
        output_file_name = os.path.basename(file_path)
        output_path = os.path.join(removedbg_folder, output_file_name)
        cv2.imwrite(output_path, output_image)

        print(f"Saved output to: {output_path}")

print("Processing complete!")