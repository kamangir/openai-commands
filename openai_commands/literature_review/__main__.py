import argparse
from blueness import module
from openai_commands import NAME, VERSION
from openai_commands.literature_review.functions import review_literature
from openai_commands.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--filename",
    type=str,
    default="review.csv",
    help="<review.csv>",
)
parser.add_argument(
    "--questions",
    type=str,
    default="questions.yaml",
    help="<questions.yaml>",
)
parser.add_argument(
    "--count",
    type=int,
    default=10,
    help="-1: all",
)
args = parser.parse_args()

success = review_literature(
    object_name=args.object_name,
    filename=args.filename,
    questions_filename=args.questions,
    count=args.count,
)

sys_exit(logger, NAME, "-", success)
