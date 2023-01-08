import os
import openai
from . import NAME
from abcli.logging import crash_report
from abcli import logging
import logging

logger = logging.getLogger(__name__)

api_key = os.getenv("OPENAI_API_KEY")


def generate_image(
    filename,
    prompt,
    n=1,
    size="1024x1024",
):
    if not api_key:
        logger.error(
            f"{NAME}.generate: API key not found, trying exporting OPENAI_API_KEY."
        )
        return False

    logger.info(f"{NAME}.generate({prompt}) -> {filename}")

    try:
        openai.api_key = api_key

        openai.Image.create_edit(
            image=open(filename, "rb"),
            prompt=prompt,
            n=n,
            size=size,
        )
    except:
        crash_report(f"-{NAME}: failed.")
        return False

    return True
