import os
import pytest
from abcli import file
from abcli.modules import objects
from openai_cli.gpt.chat import chat_with_openai, interact_with_openai, list_models


def test_chat_with_openai():
    object_name = objects.unique_object()
    object_path = objects.object_path(object_name=object_name)

    assert chat_with_openai(
        object_path=object_path,
        script_mode=True,
        script=["help", "version", "describe mathematics"],
    )

    assert file.exist(
        os.path.join(object_path, f"{object_name}.yaml"),
    )


@pytest.mark.parametrize(
    [
        "prompt",
    ],
    [
        ["describe mathematics"],
    ],
)
def test_interact_with_openai(prompt: str):
    object_name = objects.unique_object()
    object_path = objects.object_path(object_name=object_name)

    assert interact_with_openai(
        prompt=prompt,
        object_path=object_path,
    )

    assert file.exist(
        os.path.join(object_path, f"{object_name}.yaml"),
    )


def test_list_models():
    assert list_models()
