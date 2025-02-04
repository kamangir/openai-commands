from typing import List
import pytest

from openai_commands.prompt_completion.api import generate_text


@pytest.mark.parametrize(
    ["prompt", "max_tokens", "verbose"],
    [
        ("Write a tag line for an cafe in Vancouver", 1000, True),
        ("Write a tag line for an cafe in Vancouver", 1000, False),
    ],
)
def test_generate_text_prompt(
    prompt: str,
    max_tokens: int,
    verbose: bool,
):
    result = generate_text(
        prompt=prompt,
        max_tokens=max_tokens,
        verbose=verbose,
    )

    assert isinstance(result, tuple)
    assert len(result) == 3

    assert result[0] is True
    assert isinstance(result[1], str)
    assert isinstance(result[2], dict)


@pytest.mark.parametrize(
    ["messages", "max_tokens", "verbose"],
    [
        (
            ...,
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
    result = generate_text(
        messages=messages,
        max_tokens=max_tokens,
        verbose=verbose,
    )

    assert isinstance(result, tuple)
    assert len(result) == 3

    assert result[0] is True
    assert isinstance(result[1], str)
    assert isinstance(result[2], dict)
