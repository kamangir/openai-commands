import json
from openai import OpenAI
from abcli import file
from typing import Tuple, Any
from abcli.modules import host
from abcli import string
from abcli.modules import objects
from openai_cli.images import NAME
from openai_cli import VERSION
from abcli.modules.cookie import cookie
from abcli.modules.host import is_jupyter
from IPython.display import Image, display
from abcli.plugins import graphics
import abcli.logging
import logging

logger = logging.getLogger()


class OpenAIImageGenerator(object):
    def __init__(self, verbose: bool = False):
        self.client = OpenAI(api_key=cookie["openai_api_key"])
        self.verbose = verbose
        logger.info(self.__class__.__name__)

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
            model="dall-e-3",
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
                    " | ".join(objects.signature(filename)),
                ],
                [
                    prompt,
                    response.data[0].revised_prompt,
                    " | ".join(
                        [
                            f"{NAME}-{VERSION}",
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
                "I NEED to test how the tool works with extremely simple prompts.",
                "DO NOT add any detail, just use this prompt AS-IS and do not revise it:",
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
