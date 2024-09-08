from typing import Tuple, Any, Dict
from openai import OpenAI
from blueness import module
from blue_options.host import is_jupyter
from openai_commands import env
from openai_commands import NAME
from openai_commands.logger import logger

NAME = module.name(__file__, NAME)


# https://github.com/openai/openai-python
# https://github.com/openai/openai-python/discussions/742
def complete_prompt(
    prompt: str,
    max_tokens: int = 2000,
    verbose=None,
) -> Tuple[bool, str, Dict[str, Any]]:
    client = OpenAI(api_key=env.OPENAI_API_KEY)

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=env.OPENAI_GPT_DEFAULT_MODEL,
            max_tokens=max_tokens,
        )
    except Exception as e:
        logger.info(
            "{}.complete_prompt failed: {}, prompt length: {}".format(
                NAME,
                str(e),
                len(prompt),
            )
        )
        return False, str(e), {"exception": str(e)}

    if is_jupyter() if verbose is None else verbose:
        logger.info("response: {}".format(response))

    if not response.choices:
        logger.info(f"{NAME}.complete(): no choice.")
        return False, "", {"status": "no choice"}

    if len(response.choices) > 1 and verbose:
        logger.info(
            "{} choices, picked the first, and ignored the rest.".format(
                len(response.choices)
            )
        )

    choice = response.choices[0]

    metadata = {
        "response": response,
        "status": f"choice: {choice.finish_reason}",
    }

    if verbose:
        logger.info(f"{NAME}.complete(): finish_reason: {choice.finish_reason}.")
    return choice.finish_reason == "stop", choice.message.content, metadata
