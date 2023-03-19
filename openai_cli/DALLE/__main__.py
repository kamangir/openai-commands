import argparse
from abcli import file
from tqdm import tqdm
from openai_cli.DALLE import NAME
from openai_cli.DALLE.canvas import Canvas
from openai_cli import VERSION
from abcli import logging
import logging

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="render",
)
parser.add_argument(
    "--filename",
    type=str,
)
parser.add_argument(
    "--brush",
    type=str,
    help="tiling|randomwalk",
    default="tiling",
)
parser.add_argument(
    "--lines",
    type=int,
    help="-1: disable",
)
parser.add_argument(
    "--verbose",
    type=int,
    help="0|1",
    default=0,
)
parser.add_argument(
    "--dryrun",
    type=int,
    help="0|1",
    default=1,
)
args = parser.parse_args()

success = False
if args.task == "render":
    success, content = file.load_text(args.filename)

    if success:
        canvas = Canvas(
            content=content,
            dryrun=args.dryrun == 1,
            verbose=args.verbose == 1,
        )

        canvas.render_text(
            canvas.create_brush(args.brush),
            content[: args.lines] if args.lines != -1 else content,
            file.set_extension(args.filename, "png"),
        )

else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
