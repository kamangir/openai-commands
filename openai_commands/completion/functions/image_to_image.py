import os
import matplotlib.pyplot as plt

from blue_options import string
from blue_options.host import is_jupyter
from blue_objects import file
from blue_objects.env import HOME

from openai_commands.completion.functions.python import ai_function_py
from openai_commands.logger import logger


class i2i_function(ai_function_py):
    def __init__(
        self,
        *args,
        plot=None,
        **kwargs,
    ):
        super().__init__(
            *args,
            output_class_name="ndarray",
            **kwargs,
        )

        self.auto_save = True
        self.plot = is_jupyter() if plot is None else plot

        if self.validation_input is None:
            _, self.validation_input = file.load_image(
                os.path.join(
                    HOME,
                    "git/blue-bracket/images/portal-34.jpg",
                )
            )

    def compute(self, inputs):
        if self.function_handle is None:
            return None

        logger.info(
            "{}.compute({})".format(
                self.__class__.__name__,
                string.pretty_shape_of_matrix(inputs),
            )
        )

        output_image = super().compute(inputs)

        logger.info(
            "->{}".format(
                string.pretty_shape_of_matrix(output_image),
            )
        )

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
