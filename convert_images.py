import os
from PIL import Image

def convert_png_to_jpeg(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            file_path = os.path.join(directory, filename)
            # Open the image
            with Image.open(file_path) as img:
                # Convert the image to RGB mode (JPEG doesn't support alpha channel as in PNG)
                rgb_img = img.convert('RGB')
                # Save the image with a .jpeg extension
                out_path = os.path.join(directory, 'jpeg', filename[:-4] + '.jpeg')
                # print(out_path)
                rgb_img.save(out_path)
                print(f"Converted '{filename}' to JPEG format.")

# Replace 'your_directory_path' with the path of your folder
convert_png_to_jpeg('./images')
