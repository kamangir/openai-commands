from typing import List
import abcli.logging
import logging

logger = logging.getLogger()


class structured_prompt(object):
    def __init__(
        self,
        inputs: List[str],
        requirements: List[str],
        returns: List[str],
    ):
        self.inputs = inputs
        self.returns = returns
        self.requirements = requirements

    def create(
        self,
        function_name: str,
    ) -> str:
        output = "\n".join(
            ["Write a python function named {} that".format(function_name)]
            + (
                [
                    " inputs {} and".format(" and\n".join(self.inputs)),
                ]
                if self.inputs
                else []
            )
            + (
                [" {} and".format(" and\n".join(self.requirements))]
                if self.requirements
                else []
            )
            + [
                " returns {}.".format(" and\n".join(self.returns)),
            ]
        )

        while "  " in output:
            output = output.replace("  ", " ")

        logger.info(output)
        return output
