import json
from openai import OpenAI
from typing import Tuple, Any, List
from IPython.display import Image, display

from blueness import module
from blue_options import string
from blue_options.host import is_jupyter
from blue_objects import file, objects, path
from blue_objects.graphics.signature import sign_filename

from openai_commands import NAME
from openai_commands.host import signature
from openai_commands import env
from openai_commands.logger import logger


NAME = module.name(__file__, NAME)


def generate_image(
    prompt: str,
    filename: str,
    object_name: str,
    model="dall-e-3",
    sign: bool = True,
    line_width: int = 80,
    quality: str = "standard",
    size: str = "1024x1024",
    sign_with_prompt: bool = True,
    footer: List[str] = [],
    verbose: bool = False,
) -> Tuple[bool, Any]:
    assert env.OPENAI_API_KEY

    client = OpenAI(api_key=env.OPENAI_API_KEY)

    full_filename = objects.path_of(
        filename=filename,
        object_name=object_name,
    )

    logger.info(
        "{}.generate_image: {} -> {}/{}".format(
            NAME,
            prompt,
            object_name,
            filename,
        )
    )

    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        quality=quality,
        n=1,
    )

    logger.info(json.dumps(response.model_dump(), indent=4))

    success = file.download(response.data[0].url, full_filename)

    if success and sign:
        success, image = file.load_image(full_filename)

    if success and sign:
        success = sign_filename(
            filename=full_filename,
            header=[
                " | ".join(
                    objects.signature(
                        info=filename,
                        object_name=object_name,
                    )
                    + [
                        string.pretty_shape_of_matrix(image),
                        f"quality: {quality}",
                    ]
                ),
            ],
            footer=[
                " | ".join(
                    footer
                    + ([f"prompt: {prompt}"] if sign_with_prompt else [])
                    + (
                        [f"revised prompt: {str(response.data[0].revised_prompt)}"]
                        if verbose
                        else []
                    )
                    + [f"model: {model}"]
                    + signature()
                ),
            ],
            line_width=line_width,
        )

    if success and verbose and is_jupyter():
        display(Image(filename=full_filename))

    return (
        success,
        response,
    )
