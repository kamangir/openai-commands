import pytest
from openai_commands.images.api import OpenAIImageGenerator
from abcli import string
from abcli.modules import objects


@pytest.mark.parametrize(
    "prompt",
    [
        ("a person flying through the streets of Vancouver."),
    ],
)
def test_images(prompt):
    generator = OpenAIImageGenerator(verbose=False)

    object_name = objects.unique_object("test")
    filename = objects.path_of(
        f"{string.timestamp()}.png",
        object_name,
    )

    success, _ = generator.generate(
        prompt=prompt,
        filename=filename,
    )

    assert success
