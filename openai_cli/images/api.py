import json
from openai import OpenAI
from abcli.modules.cookie import cookie
import abcli.logging
import logging

logger = logging.getLogger()


class OpenAIImageGenerator(object):
    def __init__(self):
        self.client = OpenAI(api_key=cookie["openai_api_key"])
        logger.info(self.__class__.__name__)

    def generate(self, prompt):
        prompt = self.make_safe(prompt)

        logger.info(
            "{}.generate({})".format(
                self.__class__.__name__,
                prompt,
            )
        )

        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        logger.info(json.dumps(response.dict(), indent=4))

        return response

    def make_safe(self, prompt: str) -> str:
        # https://community.openai.com/t/api-image-generation-in-dall-e-3-changes-my-original-prompt-without-my-permission/476355
        return " ".join(
            [
                "I NEED to test how the tool works with extremely simple prompts.",
                "DO NOT add any detail, just use this prompt AS-IS and do not revise it:",
                prompt,
            ]
        )
