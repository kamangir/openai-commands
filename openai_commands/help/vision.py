from typing import List

from blue_options.terminal import show_usage, xtra


def help_vision(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "detail=<detail>",
            xtra(",dryrun,~upload", mono=mono),
        ]
    )

    image_options = "Davie,~Bute,.jpg"

    args = [
        "[--max_count <-1>]",
        "[--verbose 1]",
    ]

    return show_usage(
        [
            "@openai",
            "vision",
            f"[{options}]",
            f"[{image_options}]",
            '"<prompt>"',
            "[.|<object-name>]",
        ]
        + args,
        "complete <prompt> given the image(s) in <object-name>.",
        {
            "detail: auto | low | high": [],
        },
        mono=mono,
    )
