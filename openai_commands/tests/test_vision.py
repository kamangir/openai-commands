import pytest
from blue_options.options import Options
from abcli.plugins.testing import download_object
from openai_commands import env
from openai_commands.vision.completion import complete_object


@pytest.mark.skip(reason="fails.")
@pytest.mark.parametrize(
    [
        "object_name",
    ],
    [
        [env.OPENAI_COMMANDS_VISION_TEST_OBJECT],
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
