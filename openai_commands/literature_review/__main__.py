import argparse
import base64
from blueness import module
from openai_commands import NAME, VERSION
from openai_commands.literature_review.functions import review_literature
from openai_commands.literature_review.multiple import (
    generate_workflow as generate_multiple_review_workflow,
)
from openai_commands.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    default="",
    help="generate_multiple_review_workflow|review",
)
parser.add_argument(
    "--args",
    type=str,
)
parser.add_argument(
    "--question_filename",
    type=str,
    default="question1.yaml",
    help="<question.yaml>",
)
parser.add_argument(
    "--count",
    type=int,
    default=10,
    help="-1: all",
)
parser.add_argument(
    "--do_publish",
    type=int,
    default=0,
    help="0|1",
)
parser.add_argument(
    "--filename",
    type=str,
    default="",
    help="<review.csv>",
)
parser.add_argument(
    "--input_object_name",
    type=str,
)
parser.add_argument(
    "--job_name",
    type=str,
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--output_object_name",
    type=str,
)
parser.add_argument(
    "--overwrite",
    type=int,
    default=0,
    help="0|1",
)
parser.add_argument(
    "--review_options",
    type=str,
    default="",
    help="dryrun,publish",
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

success = False
if args.task == "generate_multiple_review_workflow":
    success = generate_multiple_review_workflow(
        job_name=args.job_name,
        object_name=args.object_name,
        options=args.review_options,
        do_publish=args.do_publish == 1,
        suffix=args.suffix,
        args=base64.b64decode(args.args).decode("utf-8"),
    )
elif args.task == "review":
    success = review_literature(
        count=args.count,
        filename=args.filename,
        input_object_name=args.input_object_name,
        output_object_name=args.output_object_name,
        overwrite=args.overwrite == 1,
        question_filename=args.question_filename,
        suffix=args.suffix,
        verbose=args.verbose == 1,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
