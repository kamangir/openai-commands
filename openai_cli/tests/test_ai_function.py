import os.path
from openai_cli.completion.functions.generic import ai_function
from openai_cli.completion.prompts.structured import structured_prompt
from abcli import file


def test_ai_function():
    prompt = structured_prompt(
        inputs=["a number"],
        returns=["that number plus 12"],
        requirements=["returns 0 if the input is less than 10"],
    )

    func = ai_function(
        output_class_name="int",
        verbose=True,
    )

    success = func.generate(prompt.create(func.function_name))[0]
    assert success

    value = func.compute(11)
