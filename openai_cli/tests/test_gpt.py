import os
from abcli import file
from abcli.modules import objects
from openai_cli.gpt.chat import chat_with_openai, list_models


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


def test_list_models():
    assert list_models()
