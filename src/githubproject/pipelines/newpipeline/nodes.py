"""
This is a boilerplate pipeline 'newpipeline'
generated using Kedro 0.19.8
"""

from PIL import Image, ImageDraw

#creating a function that converts the colored image to grayscale image.
def grayscaled_image(image:Image.Image)->Image.Image:
    image = image.convert("L")
    return image
def resized_image(image:Image.Image)->Image.Image:
    image = image.resize((300, 300))
    return image
def addtext(image:Image.Image)->Image.Image:
    draw = ImageDraw.Draw(image)
    text = "I am grayscaled image"
    font_size = 20
    position = (10,200)
    draw.text(position, fill = "red", text=text )
    return image















