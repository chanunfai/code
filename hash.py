import hashlib
from PIL import Image
import numpy as np
import io
import time

def calculate_md5(image_bytes):
    return hashlib.md5(image_bytes).hexdigest()

def image_to_bytes(image):
    with io.BytesIO() as output:
        image.save(output, format="PNG")
        return output.getvalue()

def modify_and_find_hash(image_path, start_number):
    start_time = time.time()  # Start the timer

    image = Image.open(image_path)
    pixels = np.array(image)

    start_number_str = str(start_number)

    original_pixel = pixels[0, 0].copy()

    for r in range(256):
        for g in range(256):
            for b in range(256):
                pixels[0, 0][:3] = [r, g, b]  # Only modify the RGB values, leave the alpha unchanged if it exists
                modified_image = Image.fromarray(pixels)
                image_bytes = image_to_bytes(modified_image)
                md5_hash = calculate_md5(image_bytes)
                if md5_hash.startswith(start_number_str):
                    end_time = time.time()  # Stop the timer
                    print(f"Found hash: {md5_hash} with pixel (0,0) = ({r}, {g}, {b})")
                    print(f"Time taken: {end_time - start_time} seconds")
                    return modified_image, md5_hash

    # Restore original pixel value
    pixels[0, 0] = original_pixel

    end_time = time.time()  # Stop the timer
    print("No hash found that starts with the specified number.")
    print(f"Time taken: {end_time - start_time} seconds")
    return None, None

def verify_md5(image_path, expected_md5):
    with open(image_path, "rb") as f:
        image_bytes = f.read()
        md5_hash = calculate_md5(image_bytes)
    return md5_hash == expected_md5

# Modify the path to your image and the starting number
image_path = 'output_image_with_hidden_message.png'
start_number = 63

# Find the image and hash
modified_image, found_hash = modify_and_find_hash(image_path, start_number)

if modified_image and found_hash:
    # Save the modified image
    modified_image.save('modified_image.png')
    print(f"Modified image saved. MD5 hash: {found_hash}")

    # Verify the MD5 hash of the saved image
    verification = verify_md5('modified_image.png', found_hash)
    print(f"Verification of saved image MD5 hash: {'Success' if verification else 'Failed'}")
