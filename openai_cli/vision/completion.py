from typing import List
from enum import Enum, auto
from abcli.options import Options
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
    options: Options(),
    max_count: int = 5,
    detail: Detail = Detail.AUTO,
    verbose: bool = False,
):
    logger.info(
        '{}.complete_object[{}]: "{}" @ {} < {} : {}'.format(
            NAME,
            detail,
            prompt,
            options.to_str(),
            max_count,
            object_name,
        )
    )

    # find the images on the cloud that options + ~inference
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
        '{}.complete[{}]: "{}" @ {}'.format(
            NAME,
            detail,
            prompt,
            len(list_of_image_urls),
        )
    )
    return False
