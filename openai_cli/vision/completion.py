from typing import List
from enum import Enum, auto
from openai_cli.vision import NAME
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class Detail(Enum):
    AUTO = auto()
    LOW = auto()
    HIGH = auto()


def complete_object(
    prompt: str,
    object_name: str,
    prefix: str,
    count: int = 2,
    extension: str = "jpg",
    detail: Detail = Detail.AUTO,
    verbose: bool = False,
):
    logger.info(
        '{}.complete_object: "{}" {}.{} @ {}: {}/{}'.format(
            NAME,
            prompt,
            count,
            extension,
            detail,
            object_name,
            prefix,
        )
    )

    # find the images on the cloud
    # aws s3 cp them to public
    list_of_image_urls = ["wip"]

    return complete(
        prompt=prompt,
        detail=detail,
        list_of_image_urls=list_of_image_urls,
        verbose=verbose,
    )


def complete(
    prompt: str,
    list_of_image_urls: List[str],
    detail: Detail = Detail.AUTO,
    verbose: bool = False,
):
    logger.info(
        '{}.complete: "{}" {} @ {}'.format(
            NAME,
            prompt,
            len(list_of_image_urls),
            detail,
        )
    )
    return False
