"""
This is a boilerplate pipeline 'newpipeline'
generated using Kedro 0.19.8
"""

from PIL import Image

#creating a function that converts the colored image to grayscale image.
def grayscaled_image(image:Image.Image)->Image.Image:
    image = image.convert("L")
    return image
def resized_image(image:Image.Image)->Image.Image:
    image = image.resize((300, 300))
    return image















