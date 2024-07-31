import pytest
from abcli.plugins.testing import download_object
from openai_commands import env
from openai_commands.literature_review.functions import review_literature


@pytest.mark.parametrize(
    ["object_name", "filename", "questions", "count"],
    [
        [
            env.LITERATURE_REVIEW_OBJECT,
            env.LITERATURE_REVIEW_TEST_FILENAME,
            env.LITERATURE_REVIEW_TEST_QUESTIONS,
            2,
        ],
    ],
)
def test_literature_review(
    object_name: str,
    filename: str,
    questions: str,
    count: int,
):
    assert download_object(object_name)

    assert review_literature(
        object_name=object_name,
        filename=filename,
        questions=questions,
        count=count,
    )
