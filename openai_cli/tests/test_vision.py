import pytest
from abcli.options import Options
from abcli.plugins.testing import download_object
from openai_cli import env
from openai_cli.vision.completion import complete_object


@pytest.mark.parametrize(
    [
        "object_name",
    ],
    [
        [env.OPENAI_VISION_TEST_OBJECT],
    ],
)
def test_vision_complete(object_name):
    assert download_object(object_name)

    assert isinstance(
        complete_object(
            object_name=object_name,
            options=Options("Arbutus16"),
            prompt="describe these images",
        ),
        bool,
    )
