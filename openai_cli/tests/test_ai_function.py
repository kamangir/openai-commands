import os.path
from openai_cli.completion.functions.generic import ai_function
from abcli import file


def test_complete_prompt():
    func = ai_function(
        inputs=["a number"],
        returns=["that number plus 12"],
        requirements=[
            "returns 0 if the input is less than 10",
        ],
        output_class_name="int",
        verbose=True,
    )

    value = func.compute(11)
