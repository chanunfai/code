from PIL import Image
import numpy as np

def decode_image(encoded_image_path, color_channel='green'):
    # Load the encoded image
    encoded_image = Image.open(encoded_image_path)
    encoded_image_array = np.array(encoded_image)
    
    # Select the appropriate color channel
    if color_channel == 'red':
        channel_data = encoded_image_array[:, :, 0]
    elif color_channel == 'green':
        channel_data = encoded_image_array[:, :, 1]
    elif color_channel == 'blue':
        channel_data = encoded_image_array[:, :, 2]
    else:
        raise ValueError("Color channel must be 'red', 'green', or 'blue'")
    
    # Decode the hidden image from the selected channel
    hidden_image = (channel_data % 2) * 255
    
    # Convert the array back to an image
    hidden_image_pil = Image.fromarray(hidden_image.astype(np.uint8))
    
    # Save or display the hidden image
    hidden_image_pil.save(f'decoded_image_from_{color_channel}_channel.png')
    hidden_image_pil.show()

# Example usage:
encoded_image_path = 'output_image_with_hidden_message.png'  # Replace with your encoded image path
decode_image(encoded_image_path, color_channel='green') 