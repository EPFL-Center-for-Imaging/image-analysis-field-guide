import os
import sys
from PIL import Image

def convert_png_to_jpeg(directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            file_path = os.path.join(directory, filename)
            with Image.open(file_path) as img:
                rgb_img = img.convert('RGB')
                out_path = os.path.join(directory, 'jpeg', filename[:-4] + '.jpeg')
                if not os.path.exists(out_path):
                    rgb_img.save(out_path)
                    print(f"Converted '{filename}' to JPEG format.")

if __name__=='__main__':
    _, directory = sys.argv  # Example folder: './images'
    convert_png_to_jpeg(directory)
