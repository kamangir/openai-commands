import argparse
from openai_cli.vision import NAME
from openai_cli import VERSION
from abcli import logging
import logging

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="<task>",
)
parser.add_argument(
    "--filename",
    type=str,
)
args = parser.parse_args()

success = False
if args.task == "<task>":
    success = True
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
