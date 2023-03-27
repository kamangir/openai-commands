import argparse
from abcli import file
from tqdm import tqdm
from aiart import html
from abcli.options import Options
from abcli.modules import objects
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
    "--source",
    type=str,
)
parser.add_argument(
    "--destination",
    type=str,
)
parser.add_argument(
    "--options",
    type=str,
    help="brush=tiling|randomwalk,~dryrun,lines=-1,url,verbose",
)
args = parser.parse_args()

success = False
if args.task == "render":
    options = Options(args.options)
    brush_kind = options.get("brush", "tiling")
    dryrun = options.get("dryrun", 1) == 1
    is_url = options.get("url", 0) == 1
    lines = options.get("lines", -1)
    verbose = options.get("verbose", 0) == 1

    if is_url:
        success, content = html.ingest_url(args.source)
    else:
        success, content = file.load_text(args.source)

    output_filename = args.destination
    if not output_filename:
        if not is_url:
            output_filename = file.set_extension(args.source, "png")
        else:
            output_filename = objects.path_of("DALL-E.png")

    if success:
        logger.info(
            f"DALL-E: render: {args.source} -{len(content)} lines-> {output_filename}"
        )

        canvas = Canvas(
            source=args.source,
            content=content,
            dryrun=dryrun,
            verbose=verbose,
        )

        canvas.render_text(
            canvas.create_brush(brush_kind),
            content[:lines] if lines != -1 else content,
            output_filename,
        )

else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
