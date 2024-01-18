from openai_cli.completion.functions.python import ai_function_py
from openai_cli.completion.prompts.structured import structured_prompt


def test_ai_function_py():
    prompt = structured_prompt(
        inputs=["a number"],
        returns=["that number plus 12"],
        requirements=["returns 0 if the input is less than 10"],
    )

    func = ai_function_py(
        output_class_name="int",
        validation_input=10,
    )

    assert func.generate(prompt.create(func.function_name))[0]
