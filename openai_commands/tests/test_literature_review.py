import pytest

from blue_objects import file, objects

from openai_commands import env
from openai_commands.literature_review.functions import (
    generate_prompt,
    review_literature,
)


@pytest.mark.parametrize(
    [
        "object_name",
        "question",
    ],
    [
        [
            env.LITERATURE_REVIEW_OBJECT,
            env.LITERATURE_REVIEW_TEST_QUESTION,
        ],
    ],
)
def test_generate_prompt(
    object_name: str,
    question: str,
):
    assert objects.download(object_name)

    success, question_dict = file.load_yaml(
        objects.path_of(
            f"{question}.yaml",
            object_name,
        )
    )
    assert success

    assert generate_prompt(question_dict)


@pytest.mark.parametrize(
    [
        "input_object_name",
        "filename",
        "question",
        "count",
    ],
    [
        [
            env.LITERATURE_REVIEW_OBJECT,
            env.LITERATURE_REVIEW_TEST_FILENAME,
            env.LITERATURE_REVIEW_TEST_QUESTION,
            2,
        ],
        [
            env.LITERATURE_REVIEW_OBJECT,
            "{}.csv".format(env.LITERATURE_REVIEW_TEST_FILENAME),
            env.LITERATURE_REVIEW_TEST_QUESTION,
            2,
        ],
    ],
)
def test_literature_review(
    input_object_name: str,
    filename: str,
    question: str,
    count: int,
):
    output_object_name = objects.unique_object("test")

    assert objects.download(input_object_name)

    assert review_literature(
        input_object_name=input_object_name,
        output_object_name=output_object_name,
        filename=filename,
        question=question,
        count=count,
    )
