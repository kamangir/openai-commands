import os
from typing import List
from abcli import file
import matplotlib.pyplot as plt
from openai_cli.completion.functions.generic import ai_function
from abcli import string
import abcli.logging
import logging

logger = logging.getLogger()


class i2i_function(ai_function):
    def __init__(
        self,
        returns: str,
        *args,
        plot: bool = False,
        requirements: List[str] = None,
        **kwargs,
    ):
        super().__init__(
            inputs=["an image as a numpy array"],
            requirements=[
                "does not run a for loop on the pixels",
                "uses numpy vector functions",
                "imports all modules that are used in the code",
                "type-casts the output correctly",
            ]
            + ([] if requirements is None else requirements),
            returns=[f"{returns} as a numpy array"],
            *args,
            output_class_name="ndarray",
            **kwargs,
        )

        self.plot = plot
        self.input_image = file.load_image(
            os.path.join(
                os.getenv("HOME", ""),
                "git/blue-bracket/images/portal-34.jpg",
            )
        )[1]

    def compute(self, inputs):
        if self.function_handle is None:
            return None

        logger.info(
            "{}.compute({})".format(
                self.__class__.__name__,
                string.pretty_shape_of_matrix(self.input_image),
            )
        )

        output_image = super().compute(inputs)

        if self.plot:
            _, axes = plt.subplots(1, 2, figsize=(10, 5))
            axes[0].imshow(inputs)
            axes[0].axis("off")
            axes[0].set_title("input image")

            axes[1].imshow(output_image)
            axes[1].axis("off")
            axes[1].set_title("output image")
            plt.subplots_adjust(wspace=0.1)
            plt.show()

        return output_image

    def generate(
        self,
        *args,
        **kwargs,
    ) -> bool:
        return super().generate(
            *args,
            validation_input=self.input_image,
            **kwargs,
        )
