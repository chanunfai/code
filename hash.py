import hashlib
import time
from PIL import Image

def calculate_md5(image_path):
    with open(image_path, "rb") as f:
        image_bytes = f.read()
        md5_hash = hashlib.md5(image_bytes).hexdigest()
    return md5_hash

def modify_and_find_hash(image_path, start_number):
    start_time = time.time()  # Start the timer
    
    image = Image.open(image_path).convert("RGB")  # Convert to RGB to avoid RGBA issue
    pixels = image.load()

    start_number_str = str(start_number)
    temp_path = "temp_image.png"  # Use PNG to avoid compression artifacts

    for r in range(256):
        for g in range(256):
            for b in range(256):
                pixels[0, 0] = (r, g, b)
                # Save the modified image to a temporary file
                image.save(temp_path)
                md5_hash = calculate_md5(temp_path)
                if md5_hash.startswith(start_number_str):
                    end_time = time.time()  # End the timer
                    elapsed_time = end_time - start_time  # Calculate elapsed time
                    print(f"Found hash: {md5_hash} with pixel (0,0) = ({r}, {g}, {b})")
                    print(f"Time taken: {elapsed_time:.2f} seconds")
                    return image, md5_hash

    end_time = time.time()  # End the timer
    elapsed_time = end_time - start_time  # Calculate elapsed time
    print("No hash found that starts with the specified number.")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    return None, None

def verify_md5(image_path, expected_md5):
    md5_hash = calculate_md5(image_path)
    return md5_hash == expected_md5

# Modify the path to your image and the starting number
image_path = 'output_image_with_hidden_message.png'
start_number = 62

# Find the image and hash
modified_image, found_hash = modify_and_find_hash(image_path, start_number)

if modified_image and found_hash:
    # Save the modified image
    modified_image_path = 'modified_image.png'
    modified_image.save(modified_image_path)
    print(f"Modified image saved. MD5 hash: {found_hash}")

    # Verify the MD5 hash of the saved image
    verification = verify_md5(modified_image_path, found_hash)
    print(f"Verification of saved image MD5 hash: {'Success' if verification else 'Failed'}")
