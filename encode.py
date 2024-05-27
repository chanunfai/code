from PIL import Image
import numpy as np

# Load the images
image1_path = 'doge.png'  # Replace with your first image path
image2_path = 'Hi This is hidden.png'  # Replace with your second image path

# Open the first image (colored)
image1 = Image.open(image1_path)
image1_array = np.array(image1)

# Open the second image (to be hidden)
image2 = Image.open(image2_path).convert('L')  # Convert to grayscale
image2_resized = image2.resize(image1.size)  # Resize to match the first image
image2_array = np.array(image2_resized)

# Binarize the second image (0 or 255)
threshold = 128
image2_binarized = (image2_array > threshold).astype(np.uint8) * 255

# Modify the green layer of the first image based on the second image
green_channel = image1_array[:, :, 1]

# Make the green channel values even or odd
green_channel_mod = green_channel.copy()
green_channel_mod[image2_binarized == 0] = (green_channel_mod[image2_binarized == 0] // 2) * 2  # Make even
green_channel_mod[image2_binarized == 255] = ((green_channel_mod[image2_binarized == 255] // 2) * 2) + 1  # Make odd

# Combine the modified green channel back into the image
image1_array[:, :, 1] = green_channel_mod

# Convert the array back to an image
output_image = Image.fromarray(image1_array)

# Save or display the output image
output_image.save('output_image_with_hidden_message.png')
output_image.show()
