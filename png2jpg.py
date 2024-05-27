from PIL import Image

def convert_png_to_jpg(png_file, jpg_file):
    # Open an image file
    with Image.open(png_file) as image:
        # Convert the image to RGB mode
        rgb_image = image.convert('RGB')
        # Save the image as JPEG
        rgb_image.save(jpg_file, 'JPEG')

# Usage
png_file_path = 'output_image_with_hidden_message.png'
jpg_file_path = 'output_image_with_hidden_message.jpg'
convert_png_to_jpg(png_file_path, jpg_file_path)

print("Conversion complete!")
