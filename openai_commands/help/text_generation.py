from typing import List

from blue_options.terminal import show_usage


def help_generate_text(
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
            "generate_text",
            '"<prompt>"',
        ]
        + args,
        "generate text.",
        mono=mono,
    )
