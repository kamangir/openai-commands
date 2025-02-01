from typing import List

from blue_options.terminal import show_usage


def help_complete(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--max_tokens <2000>]",
        "[--verbose 1]",
    ]

    return show_usage(
        [
            "@openai",
            "complete",
            '"<prompt>"',
        ]
        + args,
        "complete <prompt>.",
        mono=mono,
    )
