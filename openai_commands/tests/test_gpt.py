import os
import pytest
from typing import List

from blue_objects import file, objects

from openai_commands.gpt.chat import chat_with_openai, interact_with_openai, list_models


def test_chat_with_openai():
    object_name = objects.unique_object()
    object_path = objects.object_path(object_name=object_name)

    script: List[str] = ["help", "version", "describe mathematics"]

    success, conversation = chat_with_openai(
        output_path=object_path,
        script_mode=True,
        script=script,
    )
    assert success
    assert len(conversation) == 1

    assert file.exists(
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

    success, answer = interact_with_openai(
        prompt=prompt,
        output_path=object_path,
    )
    assert success
    assert answer

    assert file.exist(
        os.path.join(object_path, f"{object_name}.yaml"),
    )


def test_list_models():
    assert list_models()
