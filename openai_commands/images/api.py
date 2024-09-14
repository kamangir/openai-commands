import json
from openai import OpenAI
from typing import Tuple, Any
from IPython.display import Image, display

from blueness import module
from blue_options import string, host
from blue_options.host import is_jupyter
from blue_objects import file, graphics, objects

from openai_commands import NAME, VERSION
from openai_commands import env
from openai_commands.logger import logger


NAME = module.name(__file__, NAME)


class OpenAIImageGenerator:
    def __init__(
        self,
        model="dall-e-3",
        verbose: bool = False,
    ):
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
    ) -> Tuple[bool, Any]:
        logger.info(
            "{}.generate: {}".format(
                self.__class__.__name__,
                prompt,
            )
        )

        augmented_prompt = self.augment_prompt(prompt)

        response = self.client.images.generate(
            model=self.model,
            prompt=augmented_prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        logger.info(json.dumps(response.dict(), indent=4))

        success = file.download(response.data[0].url, filename) if filename else True

        if success and sign:
            success, image = file.load_image(filename)

        if success and sign:
            image = graphics.add_signature(
                image,
                [
                    " | ".join(host.signature()),
                    " | ".join(objects.signature(file.name(filename))),
                ],
                [
                    prompt,
                    str(response.data[0].revised_prompt),
                    " | ".join(
                        [
                            f"{NAME}-{VERSION}",
                            self.model,
                            string.pretty_shape_of_matrix(image),
                        ]
                    ),
                ],
            )
            success = file.save_image(filename, image)

        if success and self.verbose and is_jupyter():
            display(Image(filename=filename))

        return (
            success,
            response,
        )

    def augment_prompt(self, prompt: str) -> str:
        # https://community.openai.com/t/api-image-generation-in-dall-e-3-changes-my-original-prompt-without-my-permission/476355
        prompt = " ".join(
            [
                "THIS IS A RAW EXECUTION. ABSOLUTELY DO NOT REVISE THIS PROMPT:",
                prompt,
            ]
        )

        if self.verbose:
            logger.info(
                "{}.augment_prompt: {}".format(
                    self.__class__.__name__,
                    prompt,
                )
            )

        return prompt
