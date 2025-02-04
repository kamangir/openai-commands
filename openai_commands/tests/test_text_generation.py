from typing import List
import pytest

from openai_commands.text_generation.api import generate_text

test_prompt = "Describe Mathematics in seven words."

test_messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": test_prompt,
            }
        ],
    }
]


@pytest.mark.parametrize(
    ["prompt", "max_tokens", "verbose"],
    [
        (test_prompt, 1000, True),
        (test_prompt, 1000, False),
    ],
)
def test_generate_text_prompt(
    prompt: str,
    max_tokens: int,
    verbose: bool,
):
    success, assessment, metadata = generate_text(
        prompt=prompt,
        max_tokens=max_tokens,
        verbose=verbose,
    )
    assert success
    assert isinstance(assessment, str)
    assert isinstance(metadata, dict)


@pytest.mark.parametrize(
    ["messages", "max_tokens", "verbose"],
    [
        (
            test_messages,
            1000,
            True,
        ),
    ],
)
def test_generate_text_messages(
    messages: List,
    max_tokens: int,
    verbose: bool,
):
    success, assessment, metadata = generate_text(
        messages=messages,
        max_tokens=max_tokens,
        verbose=verbose,
    )

    assert success
    assert isinstance(assessment, str)
    assert isinstance(metadata, dict)
