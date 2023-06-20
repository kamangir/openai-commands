from typing import List
import random
from typing import Dict, Any
from openai_cli.completion.functions import complete_prompt
import cv2
import numpy as np
from abcli.logging import crash_report
import abcli.logging
import logging

logger = logging.getLogger()


class ai_function(object):
    def __init__(
        self,
        inputs: List[str],
        returns: List[str],
        requirements: List[str],
        output_class_name: str,
        verbose: bool = False,
    ):
        self.verbose = verbose

        self.inputs = inputs
        self.returns = returns
        self.requirements = requirements
        self.output_class_name = output_class_name

        self.function_name = "ai_function_{}".format(random.randint(10000000, 99999999))

        self.prompt = self.create_prompt()
        logger.info("ai_function.prompt={}".format(self.prompt))

        self.code: List[str] = []
        self.function_handle = None
        self.metadata: Dict[str, Any] = {}

    def compute(self, inputs):
        if self.function_handle is None:
            return None

        logger.info("func_ai.compute({})".format(inputs.__class__.__name__))

        outputs = self.function_handle(inputs)

        if self.output_class_name:
            if outputs.__class__.__name__ != self.output_class_name:
                logger.error(
                    "ai_func.compute({}): {} != {}".format(
                        inputs.__class__.__name__,
                        outputs.__class__.__name__,
                        self.output_class_name,
                    )
                )
                return None

        return outputs

    def generate(self):
        self.function_handle = None

        success, self.metadata = complete_prompt(
            self.prompt,
            verbose=self.verbose,
        )
        if not success:
            return success

        self.code = self.metadata["response"]["choices"][0]["text"]
        logger.info("code: {}".format(self.code))

        try:
            exec(self.code)
        except:
            crash_report("ai_function.generate() failed.")

        for thing in locals().values():
            if hasattr(thing, "__name__") and thing.__name__ == self.function_name:
                self.function_handle = thing
                break

        return self.function_handle is not None

    def create_prompt(self) -> str:
        return "\n".join(
            [
                "Write a python function named {}".format(self.function_name),
                "that inputs {}".format(" and\n".join(self.inputs)),
                "and {}".format(" and\n".join(self.requirements)),
                "and returns {}".format(" and\n".join(self.returns)),
            ]
        )
