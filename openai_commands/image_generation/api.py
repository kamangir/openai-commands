import json
from openai import OpenAI
from typing import Tuple, Any, List
from IPython.display import Image, display

from blueness import module
from blue_options import string
from blue_options.host import is_jupyter
from blue_objects import file, objects, path
from blue_objects.graphics.signature import sign_filename

from openai_commands import NAME
from openai_commands.host import signature
from openai_commands import env
from openai_commands.logger import logger


NAME = module.name(__file__, NAME)


class OpenAIImageGenerator:
    def __init__(
        self,
        model="dall-e-3",
        verbose: bool = False,
    ):
        assert env.OPENAI_API_KEY

        self.client = OpenAI(api_key=env.OPENAI_API_KEY)
        self.verbose = verbose
        self.model = model
        logger.info(
            "{}[{}]".format(
                self.__class__.__name__,
                self.model,
            )
        )

    def generate(
        self,
        prompt: str,
        filename: str = "",
        sign: bool = True,
        line_width: int = 80,
        quality: str = "standard",
        size: str = "1024x1024",
        sign_with_prompt: bool = True,
        footer: List[str] = [],
    ) -> Tuple[bool, Any]:
        object_name = path.name(file.path(filename))

        logger.info(
            "{}.generate: {} -> {}/{}".format(
                self.__class__.__name__,
                prompt,
                object_name,
                file.name_and_extension(filename),
            )
        )

        response = self.client.images.generate(
            model=self.model,
            prompt=prompt,
            size=size,
            quality=quality,
            n=1,
        )

        logger.info(json.dumps(response.model_dump(), indent=4))

        success = file.download(response.data[0].url, filename) if filename else True

        if success and sign:
            success, image = file.load_image(filename)

        if success and sign:
            success = sign_filename(
                filename=filename,
                header=[
                    " | ".join(
                        objects.signature(
                            info=file.name_and_extension(filename),
                            object_name=object_name,
                        )
                        + [
                            string.pretty_shape_of_matrix(image),
                            f"quality: {quality}",
                        ]
                    ),
                ],
                footer=[
                    " | ".join(
                        footer
                        + ([f"prompt: {prompt}"] if sign_with_prompt else [])
                        + (
                            [f"revised prompt: {str(response.data[0].revised_prompt)}"]
                            if self.verbose
                            else []
                        )
                        + [
                            f"model: {self.model}",
                        ]
                        + signature()
                    ),
                ],
                line_width=line_width,
            )

        if success and self.verbose and is_jupyter():
            display(Image(filename=filename))

        return (
            success,
            response,
        )
