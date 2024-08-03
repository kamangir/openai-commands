import argparse
from blueness import module
from openai_commands import NAME, VERSION
from openai_commands.literature_review.functions import review_literature
from openai_commands.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "--choices",
    type=str,
    default="choices.yaml",
    help="<choices.yaml>",
)
parser.add_argument(
    "--count",
    type=int,
    default=10,
    help="-1: all",
)
parser.add_argument(
    "--filename",
    type=str,
    default="review.csv",
    help="<review.csv>",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--overwrite",
    type=int,
    default=0,
    help="0|1",
)
parser.add_argument(
    "--suffix",
    type=str,
    default="",
    help="<suffix>",
)
parser.add_argument(
    "--verbose",
    type=bool,
    default=0,
    help="0|1",
)
args = parser.parse_args()

success = review_literature(
    object_name=args.object_name,
    filename=args.filename,
    choices_filename=args.choices,
    count=args.count,
    suffix=args.suffix,
    overwrite=args.overwrite == 1,
    verbose=args.verbose == 1,
)

sys_exit(logger, NAME, "-", success)
