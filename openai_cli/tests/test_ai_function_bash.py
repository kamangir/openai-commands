import pytest
from abcli.modules.objects import select
from abcli.plugins.testing import download_object
from openai_cli import env
from openai_cli.completion.functions.bash import ai_function_bash
from openai_cli.completion.prompts.bash import bash_prompt


@pytest.mark.parametrize(
    [
        "object_name",
    ],
    [
        [env.OPENAI_FUNCTION_BASH_TEST_OBJECT],
    ],
)
def test_ai_function_bash(object_name):
    assert download_object(object_name)

    select(object_name)

    prompt = bash_prompt("ingest vancouver.")

    func = ai_function_bash("vancouver_watching")

    assert isinstance(
        func.generate(
            prompt.create(
                function_name=func.function_name,
                function_short_name="vanwatch",
            )
        )[0],
        bool,
    )
