from typing import List

from blue_options.terminal import show_usage, xtra
from blueflow.help.workflow import runner_details

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


def help_combine(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("~download,dryrun,", mono=mono),
            "publish",
            xtra(",~upload", mono=mono),
        ]
    )

    return show_usage(
        [
            "@litrev",
            "combine",
            f"[{options}]",
            "[...|<object-name-1>]",
            "[..|<object-name-2>]",
            "[.|<object-name>]",
        ],
        "<object-name-1> + <object-name-2> -> <object-name>.",
        mono=mono,
    )


def help_multiple(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("dryrun,", mono=mono),
            "publish,questions=<question1+question2+...>",
            xtra(",suffix=<suffix>", mono=mono),
        ]
    )
    workflow_options = "".join(
        [
            xtra("dryrun,", mono=mono),
            "to=<runner>",
        ]
    )
    review_options = "".join(
        [
            xtra("dryrun,", mono=mono),
            "publish",
        ]
    )

    return show_usage(
        [
            "@litrev",
            "multiple",
            f"[{options}]",
            f"[{workflow_options}]",
            f"[{review_options}]",
            f"[{LITERATURE_REVIEW_OBJECT} | <object-name>]",
        ]
        + review_args,
        "ask multiple multiple-choice questions about the list of studies in <object-name>.",
        {
            "input: <object-name>/<filename>.csv, column: Abstract.": [],
            "questions: <object-name>/<question1>.yaml, <question2>.yaml, ... .": [],
            "output: <object-name>-<suffix>-<question1>-<question-2>-<...>/<filename>.csv, columns: <question1>, <question2>, ... .": [],
            **runner_details,
        },
        mono=mono,
    )


help_functions = {
    "": help_,
    "combine": help_combine,
    "multiple": help_multiple,
}
