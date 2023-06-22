import os
import openai
from abcli.modules.cookie import cookie
from typing import Tuple, Any, Dict, List
from abcli.modules.host import is_jupyter
import abcli.logging
import logging

logger = logging.getLogger()

openai.api_key = os.environ["OPENAI_API_KEY"] = cookie["openai_api_key"]


def complete_prompt(
    prompt: str,
    max_tokens: int = 2000,
    verbose=None,
) -> Tuple[bool, str, Dict[str, Any]]:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
    )

    if is_jupyter() if verbose is None else verbose:
        logger.info("response: {}".format(response))

    if not response["choices"]:
        logger.info("openai-cli.complete(): no choice.")
        return False, "", {"status": "no choice"}

    choice = response["choices"][0]

    metadata = {
        "response": response,
        "status": f'choice: {choice["finish_reason"]}',
    }

    logger.info(
        "openai-cli.complete(): finish_reason: {}.".format(choice["finish_reason"])
    )
    return choice["finish_reason"] == "stop", choice["text"], metadata
