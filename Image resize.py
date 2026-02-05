from PIL import Image

# Function to resize an image
def resize_image(input_image_path, output_image_path, size):
    with Image.open(input_image_path) as img:
        resized_img = img.resize(size)
        resized_img.save(output_image_path)
        print(f"Image saved at {output_image_path} with size {size}")

# Usage example
resize_image("/storage/emulated/0/Download/autodraw 9_6_2024.png", "/storage/emulated/0/Download/autodraw.png", (500, 500))