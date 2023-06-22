from typing import List
import random
from typing import Dict, Any, Tuple
from openai_cli.completion.api import complete_prompt
import cv2
import skimage
from abcli.modules.host import is_jupyter
from abcli.modules import objects
from abcli import file
import numpy as np
from abcli.logging import crash_report
import abcli.logging
import logging

logger = logging.getLogger()


class ai_function(object):
    def __init__(
        self,
        output_class_name: str,
        verbose=None,
    ):
        self.verbose = is_jupyter() if verbose is None else verbose
        self.output_class_name = output_class_name

        self.function_name = "{}_{}".format(
            self.__class__.__name__,
            random.randint(10000000, 99999999),
        )

        self.code: List[str] = []
        self.function_handle = None

        self.auto_save = False

    def compute(self, inputs):
        if self.function_handle is None:
            return None

        logger.info(
            "{}.compute({})".format(
                self.__class__.__name__,
                inputs.__class__.__name__,
            )
        )

        outputs = self.function_handle(inputs)
        logger.info("-> {}".format(outputs.__class__.__name__))

        if self.output_class_name:
            if outputs.__class__.__name__ != self.output_class_name:
                logger.error(
                    "{}.compute({}): {} != {}".format(
                        self.__class__.__name__,
                        inputs.__class__.__name__,
                        outputs.__class__.__name__,
                        self.output_class_name,
                    )
                )
                return None

        return outputs

    def generate(
        self,
        prompt,
        retry: int = 5,
        validation_input=None,
    ) -> Tuple[bool, Dict[str, Any]]:
        self.function_handle = None

        success, self.code, metadata = complete_prompt(
            prompt,
            verbose=self.verbose,
        )
        if not success:
            return success, metadata

        logger.info("code: {}".format(self.code))

        try:
            exec(self.code)
        except:
            crash_report("{}.generate() failed.".format(self.__class__.__name__))

        for thing in locals().values():
            if hasattr(thing, "__name__") and thing.__name__ == self.function_name:
                self.function_handle = thing
                break

        passed = self.function_handle is not None

        if passed and validation_input is not None:
            try:
                validation_output = self.compute(validation_input)

                if validation_output is None:
                    passed = False
            except:
                crash_report("compute test failed.")
                passed = False

        if passed:
            if self.auto_save:
                self.save()
            return True, metadata

        if retry <= 0:
            logger.info("last retry, failed.")
            return False, metadata

        logger.info("{} more tries.".format(retry))
        return self.generate(retry - 1)

    def save(self, filename=""):
        if not filename:
            filename = objects.path_of(f"{self.__class__.__name__}_code.json")

        _, content = file.load_json(filename, civilized=True)

        content[self.function_name] = self.to_json()

        file.save_json(filename, content)

        logger.info(f"-> {filename}")

    def to_json(self):
        return {
            "code": self.code,
            "function_name": self.function_name,
            "output_class_name": self.output_class_name,
        }
