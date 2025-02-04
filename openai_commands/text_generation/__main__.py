import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from openai_commands import NAME
from openai_commands.text_generation.api import generate_text
from openai_commands.logger import logger

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="generate_text",
)
parser.add_argument(
    "--prompt",
    type=str,
)
parser.add_argument(
    "--max_tokens",
    type=int,
    default=2000,
)
parser.add_argument(
    "--verbose",
    type=int,
    help="0 | 1",
    default=0,
)
args = parser.parse_args()

success = False
if args.task == "generate_text":
    success, text, _ = generate_text(
        prompt=args.prompt,
        max_tokens=args.max_tokens,
        verbose=args.verbose == 1,
    )
    print(text)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
