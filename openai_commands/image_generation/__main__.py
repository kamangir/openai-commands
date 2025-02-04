import argparse
from tqdm import tqdm

from blueness import module
from blueness.argparse.generic import sys_exit
from blue_options import string
from blue_objects import file, objects

from openai_commands import NAME
from openai_commands.tests.test_text_generation import test_prompt
from openai_commands.image_generation.api import generate_image
from openai_commands.logger import logger

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="generate_image",
)
parser.add_argument(
    "--filename",
    type=str,
    default=f"{string.timestamp()}.png",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--prompt",
    type=str,
    default="",
    help=test_prompt,
)
parser.add_argument(
    "--verbose",
    type=int,
    default=0,
    help="0|1",
)
args = parser.parse_args()

success = False
if args.task == "generate_image":
    success, _ = generate_image(
        prompt=args.prompt,
        filename=args.filename,
        object_name=args.object_name,
        verbose=args.verbose,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
