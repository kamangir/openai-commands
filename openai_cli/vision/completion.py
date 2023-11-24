from enum import Enum, auto
from openai_cli.vision import NAME
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class Detail(Enum):
    AUTO = auto()
    LOW = auto()
    HIGH = auto()


def complete(
    prompt: str,
    count: int,
    detail: Detail,
    extension: str,
    object_name: str,
    prefix: str,
    verbose: bool,
):
    logger.info(
        '{}.complete: "{}" {}.{} @ {}: {}/{}'.format(
            NAME,
            prompt,
            count,
            extension,
            detail,
            object_name,
            prefix,
        )
    )

    # find the images

    # copy them to public

    return True
