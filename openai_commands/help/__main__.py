from blueness import module
from blue_options.help.functions import help_main

from openai_commands import NAME
from openai_commands.help.functions import help_functions

NAME = module.name(__file__, NAME)


help_main(NAME, help_functions)
