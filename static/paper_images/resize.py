import os
import cv2

from PIL import Image, ImageOps


def pad_image_to_aspect_ratio(image_path, output_path, desired_aspect_ratio):
    # Open the image file
    img = Image.open(image_path).convert("RGBA")
    
    # Calculate the new dimensions to maintain the aspect ratio
    img_width, img_height = img.size
    img_aspect_ratio = img_width / img_height
    
    if img_aspect_ratio > desired_aspect_ratio:
        # Image is too wide, adjust height
        new_width = img_width
        new_height = int(img_width / desired_aspect_ratio)
    else:
        # Image is too tall, adjust width
        new_height = img_height
        new_width = int(img_height * desired_aspect_ratio)
    
    # Create a new image with the desired aspect ratio and transparent background
    new_img = Image.new("RGBA", (new_width, new_height), (255, 255, 255, 0))
    
    # Paste the original image at the center of the new image
    offset_x = (new_width - img_width) // 2
    offset_y = (new_height - img_height) // 2
    new_img.paste(img, (offset_x, offset_y), img)
    
    # Save the padded image with PNG compression
    new_img.save(output_path, format="PNG", optimize=True)

ar = 1610/317 

for im in os.listdir("."):
    if ".py" not in im:
        print(im)
        pad_image_to_aspect_ratio(im, im.replace(".jpg",".png"), ar)


