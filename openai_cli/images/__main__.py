import argparse
from abcli.options import Options
from openai_cli.images import NAME
from abcli.modules import objects
from abcli import string
from openai_cli import VERSION
from openai_cli.images.api import OpenAIImageGenerator
from abcli import logging
import logging

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="generate",
)
parser.add_argument(
    "--object_name",
    type=str,
    default=".",
)
parser.add_argument(
    "--options",
    type=str,
    default="",
)
parser.add_argument(
    "--filename",
    type=str,
    default=f"{string.timestamp()}.png",
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
if args.task == "generate":
    generator = OpenAIImageGenerator(verbose=args.verbose)

    filename = objects.path_of(
        args.filename,
        object_name=args.object_name,
        create=True,
    )

    success, _ = generator.generate(
        prompt=args.prompt,
        filename=filename,
    )
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
