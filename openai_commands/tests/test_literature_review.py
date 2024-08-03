import pytest
from abcli import file
from abcli.modules import objects
from abcli.plugins.testing import download_object
from openai_commands import env
from openai_commands.literature_review.functions import (
    generate_prompt,
    review_literature,
)


@pytest.mark.parametrize(
    [
        "object_name",
        "filename",
        "choices_filename",
    ],
    [
        [
            env.LITERATURE_REVIEW_OBJECT,
            env.LITERATURE_REVIEW_TEST_FILENAME,
            env.LITERATURE_REVIEW_TEST_CHOICES,
        ],
    ],
)
def test_generate_prompt(
    object_name: str,
    filename: str,
    choices_filename: str,
):
    assert download_object(object_name)

    success, choices = file.load_yaml(
        objects.path_of(
            choices_filename,
            object_name,
        )
    )
    assert success

    assert generate_prompt(choices)


@pytest.mark.parametrize(
    [
        "object_name",
        "filename",
        "choices_filename",
        "count",
    ],
    [
        [
            env.LITERATURE_REVIEW_OBJECT,
            env.LITERATURE_REVIEW_TEST_FILENAME,
            env.LITERATURE_REVIEW_TEST_CHOICES,
            2,
        ],
    ],
)
def test_literature_review(
    object_name: str,
    filename: str,
    choices_filename: str,
    count: int,
):
    assert download_object(object_name)

    assert review_literature(
        object_name=object_name,
        filename=filename,
        choices_filename=choices_filename,
        count=count,
    )
