"""
This is a boilerplate pipeline 'newpipeline'
generated using Kedro 0.19.8
"""

from PIL import Image

#creating a function that converts the colored image to grayscale image.
def grayscale_image(image:Image.image)->Image.Image:
    image = image.convert("L")
    return image


