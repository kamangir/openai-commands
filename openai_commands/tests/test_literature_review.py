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
        "question_filename",
    ],
    [
        [
            env.LITERATURE_REVIEW_OBJECT,
            "{}.yaml".format(env.LITERATURE_REVIEW_TEST_QUESTION),
        ],
    ],
)
def test_generate_prompt(
    object_name: str,
    question_filename: str,
):
    assert download_object(object_name)

    success, instructions = file.load_yaml(
        objects.path_of(
            question_filename,
            object_name,
        )
    )
    assert success

    assert generate_prompt(instructions)


@pytest.mark.parametrize(
    [
        "input_object_name",
        "filename",
        "question_filename",
        "count",
    ],
    [
        [
            env.LITERATURE_REVIEW_OBJECT,
            env.LITERATURE_REVIEW_TEST_FILENAME,
            "{}.yaml".format(env.LITERATURE_REVIEW_TEST_QUESTION),
            2,
        ],
        [
            env.LITERATURE_REVIEW_OBJECT,
            "{}.csv".format(env.LITERATURE_REVIEW_TEST_FILENAME),
            "{}.yaml".format(env.LITERATURE_REVIEW_TEST_QUESTION),
            2,
        ],
    ],
)
def test_literature_review(
    input_object_name: str,
    filename: str,
    question_filename: str,
    count: int,
):
    output_object_name = objects.unique_object("test")

    assert download_object(input_object_name)

    assert review_literature(
        input_object_name=input_object_name,
        output_object_name=output_object_name,
        filename=filename,
        question_filename=question_filename,
        count=count,
    )
