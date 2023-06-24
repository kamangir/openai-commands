from typing import List
import abcli.logging
import logging

logger = logging.getLogger()


class ai_prompt(object):
    def __init__(
        self,
        objective: List[str],
    ):
        self.objective = objective

    def create(
        self,
        function_name: str,
    ) -> str:
        output = "\n".join(self.objective).replace("{function_name}", function_name)

        logger.info(output)
        return output
