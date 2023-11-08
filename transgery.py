from PIL import Image

# Load the uploaded image
image_path = 'test1.bmp'  # Replace with your image path
original_image = Image.open(image_path)

# Ensure image is converted to 24-bit depth, BMP format inherently is 24-bit
converted_image_path = 'converted_image.bmp'
original_image.save(converted_image_path, format='BMP')

print(f"Image saved at {converted_image_path}")
