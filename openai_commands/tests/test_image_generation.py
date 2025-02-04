import pytest

from blue_options import string
from blue_objects import objects

from openai_commands.image_generation.api import generate_image


@pytest.mark.parametrize(
    "prompt",
    [
        ("a person flying through the streets of Vancouver."),
    ],
)
def test_image_generation(prompt: str):
    success, _ = generate_image(
        prompt=prompt,
        object_name=objects.unique_object("test_image_generation"),
        filename=f"{string.timestamp()}.png",
    )

    assert success
