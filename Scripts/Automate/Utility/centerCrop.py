import os
from PIL import Image

# Define the directories
input_folder = os.path.expanduser('~/Downloads/RemovedBG')
output_folder = os.path.expanduser('~/Downloads/ProcessedImages')

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def crop_center(image, crop_width, crop_height):
    img_width, img_height = image.size
    left = (img_width - crop_width) / 2
    top = (img_height - crop_height) / 2
    right = (img_width + crop_width) / 2
    bottom = (img_height + crop_height) / 2
    return image.crop((left, top, right, bottom))

# Loop through all images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        # Get the smaller dimension to maintain 1:1 ratio
        min_dimension = min(img.size)
        
        # Crop the image centered and at 1:1 ratio
        cropped_img = crop_center(img, min_dimension, min_dimension)
        
        # Save the cropped image to the output folder
        output_path = os.path.join(output_folder, filename)
        cropped_img.save(output_path)

print("Cropping completed!")
