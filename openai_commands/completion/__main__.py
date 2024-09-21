import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from openai_commands import NAME
from openai_commands.completion.prompts.bash import bash_prompt
from openai_commands.logger import logger

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="complete|pre_process_bash_description",
)
parser.add_argument(
    "--filename",
    type=str,
)
parser.add_argument(
    "--prompt",
    type=str,
)
parser.add_argument(
    "--max_token",
    type=int,
    default=2000,
)
parser.add_argument(
    "--verbose",
    type=int,
    help="0|1",
    default=0,
)
args = parser.parse_args()

success = False
if args.task == "complete":
    from openai_commands.completion.api import complete_prompt

    success, text, _ = complete_prompt(
        args.prompt,
        args.max_token,
        args.verbose == 1,
    )
    print(text)
elif args.task == "pre_process_bash_description":
    success = bash_prompt.pre_process(args.filename)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
