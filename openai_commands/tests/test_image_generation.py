import pytest

from blue_options import string
from blue_objects import objects

from openai_commands.image_generation.api import OpenAIImageGenerator


@pytest.mark.parametrize(
    "prompt",
    [
        ("a person flying through the streets of Vancouver."),
    ],
)
def test_image_generation(prompt):
    object_name = objects.unique_object("test_image_generation")

    generator = OpenAIImageGenerator(verbose=False)

    filename = objects.path_of(
        f"{string.timestamp()}.png",
        object_name,
    )

    success, _ = generator.generate(
        prompt=prompt,
        filename=filename,
    )

    assert success
