"""
This is a boilerplate pipeline 'newpipeline'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import grayscaled_image
def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = grayscaled_image,
            inputs = "colored_image",
            outputs = "grayscaled_image1",
            name = "grayscaled_image",
        )
    ])
