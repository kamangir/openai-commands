import argparse
from blueness import module
from tqdm import tqdm
from abcli import string
from abcli.modules import objects
from abcli import file
from openai_commands import NAME, VERSION
from openai_commands.images.api import OpenAIImageGenerator
from openai_commands.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)


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
    help="prompt+prompt+prompt",
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

    success = True
    for index, prompt in tqdm(enumerate(args.prompt.split("+"))):
        filename = objects.path_of(
            filename=file.add_postfix(args.filename, f"{index:05d}"),
            object_name=args.object_name,
            create=True,
        )

        if not generator.generate(
            prompt=prompt,
            filename=filename,
        )[0]:
            success = False
else:
    success = None

sys_exit(logger, NAME, args.task, success)
