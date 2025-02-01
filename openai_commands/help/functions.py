from typing import List

from abcli.help.generic import help_functions as generic_help_functions
from blue_options.terminal import show_usage

from openai_commands import ALIAS
from openai_commands.help.complete import help_complete


def help_browse(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "actions | dashboard"

    return show_usage(
        [
            "@openai",
            "browse",
            f"[{options}]",
        ],
        "browse @openai.",
        mono=mono,
    )


help_functions = generic_help_functions(plugin_name=ALIAS)

help_functions.update(
    {
        "browse": help_browse,
        "complete": help_complete,
    }
)
