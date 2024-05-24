from openai_commands.completion.functions.generic import ai_function
from openai_commands.completion.prompts.generic import ai_prompt


def test_ai_function():
    prompt = ai_prompt(
        objective=["plan the validation of a new hardware"],
    )

    func = ai_function()

    assert func.generate(prompt.create(func.function_name))[0]
