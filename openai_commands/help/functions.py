from typing import List

from abcli.help.generic import help_functions as generic_help_functions
from blue_options.terminal import show_usage

from openai_commands import ALIAS
from openai_commands.help.image_generation import help_generate_image
from openai_commands.help.literature_review import (
    help_functions as help_literature_review,
)
from openai_commands.help.prompt_completion import help_complete
from openai_commands.help.vision import help_vision


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
        "generate_image": help_generate_image,
        "literature_review": help_literature_review,
        "vision": help_vision,
    }
)
