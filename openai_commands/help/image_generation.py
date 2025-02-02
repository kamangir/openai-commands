from typing import List

from blue_options.terminal import show_usage, xtra


def help_generate_image(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("dryrun,", mono=mono),
            "filename=<filename.png>",
            xtra(",~upload", mono=mono),
        ]
    )

    args = [
        "[--verbose 1]",
    ]

    return show_usage(
        [
            "@openai",
            "generate_image",
            f"[{options}]",
            '"<prompt>"',
            "[-|<object-name>]",
        ]
        + args,
        "<prompt> -generate-image-> <object-name>/<filename.png>.",
        mono=mono,
    )
