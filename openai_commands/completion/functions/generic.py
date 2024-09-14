from typing import List, Dict, Any, Tuple
import random

from blue_options.host import is_jupyter
from blue_objects import file, objects

from openai_commands.completion.api import complete_prompt
from openai_commands.logger import logger


class ai_function:
    def __init__(
        self,
        function_name: str = "",
        verbose=None,
    ):
        self.language = "unknown"
        self.verbose = is_jupyter() if verbose is None else verbose

        self.function_name = (
            function_name
            if function_name
            else "{}_{}".format(
                self.__class__.__name__,
                random.randint(10000000, 99999999),
            )
        )

        self.prompt: List[str] = []
        self.code: List[str] = []

        self.auto_save = False

    def generate(
        self,
        prompt,
    ) -> Tuple[bool, Dict[str, Any]]:
        self.prompt = prompt

        logger.info("prompt: {}".format(prompt))

        success, self.code, metadata = complete_prompt(
            self.prompt,
            verbose=self.verbose,
        )

        if success:
            logger.info("code: {}".format(self.code))

        return success, metadata

    def save(self, filename=""):
        if not filename:
            filename = objects.path_of(f"{self.__class__.__name__}_code.json")

        _, content = file.load_json(filename, ignore_error=True)

        content[self.function_name] = self.to_json()

        file.save_json(filename, content)

        logger.info("-> {}".format(filename))

    def to_json(self):
        return {
            "code": self.code,
            "function_name": self.function_name,
            "prompt": self.prompt,
        }
