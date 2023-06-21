import argparse
from openai_cli import NAME, VERSION
from abcli import logging
import logging

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="complete|version",
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
    from openai_cli.completion.api import complete_prompt

    success, text, _ = complete_prompt(
        args.prompt,
        args.max_token,
        args.verbose == 1,
    )
    print(text)
elif args.task == "version":
    import openai

    print(f"{NAME}-{VERSION}-{openai.version.VERSION}")
    success = True
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
