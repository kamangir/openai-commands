import argparse
import os

from blueness import module
from blueness.argparse.generic import sys_exit
from blue_options.options import Options
from blue_objects import file, objects

from articraft import html
from openai_commands import NAME
from openai_commands.DALLE.canvas import Canvas
from openai_commands.logger import logger

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="render",
)
parser.add_argument(
    "--footer",
    type=int,
    default=0,
)
parser.add_argument(
    "--header",
    type=int,
    default=0,
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
    help="brush=tiling|randomwalk,brush_size={},~dryrun,lines=-1,url,verbose".format(
        os.getenv("DALL_E_BRUSH_SIZES", "")
    ),
)

args = parser.parse_args()

success = False
if args.task == "render":
    options = Options(args.options)
    brush_kind = options.get("brush", "tiling")
    brush_size = options.get("brush_size", 256)
    dryrun = options.get("dryrun", 1) == 1
    is_url = options.get("url", 0) == 1
    lines = options.get("lines", -1)
    verbose = options.get("verbose", 0) == 1

    if is_url:
        success, content = html.ingest_poetry_from_url(
            args.source,
            args.header,
            args.footer,
        )
    else:
        success, content = file.load_text(args.source)

    output_filename = args.destination
    if not output_filename:
        if not is_url:
            output_filename = file.add_extension(args.source, "png")
        else:
            output_filename = objects.path_of("DALL-E.png")

    if success:
        content = content[:lines] if lines != -1 else content

        logger.info(
            f"DALL-E: render: {args.source} -{len(content)} lines-> {output_filename}"
        )

        canvas = Canvas(
            brush_kind=brush_kind,
            brush_size=brush_size,
            content=content,
            dryrun=dryrun,
            source=args.source,
            verbose=verbose,
        )

        canvas.render_text(
            canvas.create_brush(
                brush_kind,
                brush_size,
            ),
            content,
            output_filename,
        )

else:
    success = None

sys_exit(logger, NAME, args.task, success)
