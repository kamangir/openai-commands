import os
from enum import Enum, auto
from typing import List
from tqdm import tqdm
from openai import OpenAI
from openai_cli.completion import api_key
from abcli import file
from abcli import string
from abcli.modules import objects
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

    success, content, metadata = complete(
        prompt=prompt,
        detail=detail,
        list_of_image_urls=list_of_image_urls,
        verbose=verbose,
    )
    if not success:
        return success
    logger.info(f"🤖 {content}")

    filename = objects.path_of("openai-vision.json", object_name)
    _, past_metadata = file.load_json(filename, civilized=True)
    past_metadata[string.timestamp()] = metadata
    return file.save_json(filename, past_metadata, log=True)


# https://platform.openai.com/docs/guides/vision/multiple-image-inputs
def complete(
    prompt: str,
    list_of_image_urls: List[str],
    detail: Detail = Detail.AUTO,
    max_tokens: int = 300,
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

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    }
                ]
                + [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_urls,
                        },
                    }
                    for image_urls in list_of_image_urls
                ],
            }
        ],
        max_tokens=max_tokens,
    )

    if verbose:
        logger.info("response: {}".format(response))

    if not response.choices:
        logger.info("openai-cli.vision.complete(): no choice.")
        return False, "", {"status": "no choice"}

    if len(response.choices) > 1:
        logger.info(
            "{} choices, picked the first, and ignored the rest.".format(
                len(response.choices)
            )
        )

    choice = response.choices[0]
    logger.info(
        "openai-cli.vision.complete(): finish_reason: {}.".format(choice.finish_reason)
    )
    return (
        choice.finish_reason == "stop",
        choice.message.content,
        {
            "prompt": prompt,
            "list_of_image_urls": list_of_image_urls,
            "response": response,
            "finish_reason": choice.finish_reason,
        },
    )
