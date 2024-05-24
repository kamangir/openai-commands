import pytest
from openai_commands.completion.prompts.bash import bash_prompt
from abcli.modules import objects


@pytest.mark.parametrize(
    ["function_short_name"],
    [
        ["vanwatch"],
    ],
)
def test_pre_process(function_short_name):
    assert bash_prompt(objects.path_of(f"{function_short_name}-description.txt"))


@pytest.mark.parametrize(
    [
        "function_name",
        "function_short_name",
    ],
    [
        [
            "vancouver_watching",
            "vanwatch",
        ],
    ],
)
def test_bash_prompt(function_name, function_short_name):
    prompt = bash_prompt("ingest vancouver.")
    prompt.create(
        function_name=function_name,
        function_short_name=function_short_name,
    )
