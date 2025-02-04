import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from openai_commands import NAME
from openai_commands.prompt_completion.api import generate_text
from openai_commands.logger import logger

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="complete",
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
    success, text, _ = generate_text(
        args.prompt,
        args.max_token,
        args.verbose == 1,
    )
    print(text)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
