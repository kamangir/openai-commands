from typing import List

from blue_options.terminal import show_usage, xtra

from openai_commands.env import LITERATURE_REVIEW_OBJECT

review_args = [
    "[--count <-1>]",
    "[--filename <filename>]",
    "[--overwrite 1]",
    "[--verbose 1]",
]


def help_(
    tokens: List[str],
    mono: bool,
) -> str:

    options = "".join(
        [
            xtra("dryrun,~download,", mono=mono),
            "publish,question=<question>",
            xtra(",suffix=<suffix>,~upload", mono=mono),
        ]
    )

    return show_usage(
        [
            "@litrev",
            f"[{options}]",
            f"[{LITERATURE_REVIEW_OBJECT} | <object-name>]",
        ]
        + review_args,
        "ask a multiple-choice question about the list of studies in <object-name>.",
        {
            "input: <object-name>/<filename>.csv, column: Abstract.": [],
            "question: <object-name>/<question>.yaml.": [],
            "output: <object-name>-<suffix>-<question>/<filename>.csv, column: <question>.": [],
        },
        mono=mono,
    )


help_functions = {
    "": help_,
}
