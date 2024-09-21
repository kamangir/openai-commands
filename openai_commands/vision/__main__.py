import argparse

from blueness import module
from blueness.argparse.generic import sys_exit
from blue_options.options import Options

from openai_commands import NAME
from openai_commands.vision.completion import complete_object, Detail
from openai_commands.logger import logger

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="complete",
)
parser.add_argument(
    "--detail",
    type=str,
    default="auto",
    help="auto|low|high",
)
parser.add_argument(
    "--object_name",
    type=str,
    default="",
)
parser.add_argument(
    "--options",
    type=str,
    default="",
    help="Davie,~Bute,.jpg",
)
parser.add_argument(
    "--max_count",
    type=int,
    default=5,
)
parser.add_argument(
    "--prompt",
    type=str,
    default="",
)
parser.add_argument(
    "--verbose",
    type=int,
    default=0,
    help="0|1",
)
args = parser.parse_args()

success = False
if args.task == "complete":
    success = complete_object(
        detail=Detail[args.detail.upper()],
        max_count=args.max_count,
        object_name=args.object_name,
        options=Options(args.options),
        prompt=args.prompt,
        verbose=args.verbose,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
