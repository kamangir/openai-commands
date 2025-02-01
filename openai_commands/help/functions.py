from abcli.help.generic import help_functions as generic_help_functions

from openai_commands import ALIAS
from openai_commands.help.complete import help_complete


help_functions = generic_help_functions(plugin_name=ALIAS)

help_functions.update(
    {
        "complete": help_complete,
    }
)
