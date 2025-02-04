from typing import Tuple, Any, Dict, List
from openai import OpenAI
import pprint

from blueness import module
from blue_options.host import is_jupyter

from openai_commands import env
from openai_commands import NAME
from openai_commands.logger import logger

NAME = module.name(__file__, NAME)


# https://platform.openai.com/docs/guides/text-generation
# https://github.com/openai/openai-python
# https://github.com/openai/openai-python/discussions/742
def generate_text(
    messages: List = [],
    prompt: str = "",
    max_tokens: int = 2000,
    verbose=None,
) -> Tuple[bool, str, Dict[str, Any]]:
    if not env.OPENAI_API_KEY:
        logger.error("OPENAI_API_KEY is not set.")
        return False, "", {}

    client = OpenAI(api_key=env.OPENAI_API_KEY)

    if prompt:
        messages = [
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}],
            }
        ]
    if verbose:
        logger.info(f"messages: {pprint.pformat(messages)}")

    try:
        response = client.chat.completions.create(
            messages=messages,
            model=env.OPENAI_GPT_DEFAULT_MODEL,
            max_tokens=max_tokens,
        )
    except Exception as e:
        logger.error(e)
        return False, str(e), {"exception": str(e)}

    if is_jupyter() if verbose is None else verbose:
        logger.info("response: {}".format(response))

    if not response.choices:
        logger.info(f"{NAME}.complete(): no choice.")
        return False, "", {"status": "no choice"}

    if len(response.choices) > 1 and verbose:
        logger.info("{} choices, picked the first.".format(len(response.choices)))

    choice = response.choices[0]

    metadata = {
        "response": response,
        "status": f"choice: {choice.finish_reason}",
    }

    if verbose:
        logger.info(f"{NAME}.complete(): finish_reason: {choice.finish_reason}.")

    return choice.finish_reason == "stop", str(choice.message.content), metadata
