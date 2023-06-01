"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.9
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import preprocessing, split_data
def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=preprocessing,
             inputs="iris",
             outputs=["X","y"]),

        node(func=split_data,
             inputs=["X","y","params:spilt"],
             outputs=[ "X_train", "X_test", "y_train", "y_test"]),

    ])
