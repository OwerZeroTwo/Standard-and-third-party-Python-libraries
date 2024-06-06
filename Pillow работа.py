from PIL import Image, ImageFilter

# Open the image file
img = Image.open("image.jpg")

# Resize the image
img_resized = img.resize((300, 300))

# Apply a filter (e.g., blur)
img_filtered = img_resized.filter(ImageFilter.BLUR)

# Save the processed image
img_filtered.save("processed_image.jpg")