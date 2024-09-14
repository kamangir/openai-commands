import pytest

from blue_objects import objects

from openai_commands import env
from openai_commands.completion.functions.bash import ai_function_bash
from openai_commands.completion.prompts.bash import bash_prompt


@pytest.mark.skip(reason="select() is obsolete.")
@pytest.mark.parametrize(
    [
        "object_name",
    ],
    [
        [env.OPENAI_COMMANDS_FUNCTION_BASH_TEST_OBJECT],
    ],
)
def test_ai_function_bash(object_name):
    assert objects.download(object_name)

    # select(object_name)
    assert False

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
