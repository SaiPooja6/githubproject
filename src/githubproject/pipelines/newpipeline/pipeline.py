"""
This is a boilerplate pipeline 'newpipeline'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import grayscaled_image, resized_image, addtext
def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = grayscaled_image,
            inputs = "colored_image",
            outputs = "grayscaled_image1",
            name = "grayscaled_image",
        ),
        node(
            func = resized_image,
            inputs= "grayscaled_image1",
            outputs = "resized_image",
            name = "resized_image",
        ),
        node(
            func = addtext,
            inputs = "resized_image",
            outputs = "final_image",
            name = "addtext",
        )
    ])
