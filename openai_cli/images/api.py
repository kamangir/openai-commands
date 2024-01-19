import json
from openai import OpenAI
from abcli import file
from typing import Tuple, Any
from abcli.modules.cookie import cookie
from abcli.modules.host import is_jupyter
from IPython.display import Image, display
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
    ) -> Tuple[bool, Any]:
        logger.info(
            "{}.generate({})".format(
                self.__class__.__name__,
                prompt,
            )
        )

        prompt = self.make_safe(prompt)

        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        logger.info(json.dumps(response.dict(), indent=4))

        success = file.download(response.data[0].url, filename) if filename else True

        if self.verbose and is_jupyter():
            display(Image(filename=filename))

        return (
            success,
            response,
        )

    def make_safe(self, prompt: str) -> str:
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
                "{}.make_safe: {}".format(
                    self.__class__.__name__,
                    prompt,
                )
            )

        return prompt
