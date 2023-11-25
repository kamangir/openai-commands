from abcli.modules import objects
from abcli.plugins import aws
import os
from tqdm import tqdm
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

    options["inference"] = False
    list_of_images = objects.list_of_files(object_name, cloud=True)
    for keyword in options:
        list_of_images = [
            filename
            for filename in list_of_images
            if (keyword in filename if options[keyword] else keyword not in filename)
        ]

    url_prefix = os.getenv("abcli_publish_prefix", "")
    list_of_image_urls = [
        f"{url_prefix}/{object_name}/{image_name}"
        for image_name in tqdm(list_of_images)
    ]
    logger.info(
        "{} images: {}".format(
            len(list_of_image_urls),
            ", ".join(list_of_image_urls),
        )
    )

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
