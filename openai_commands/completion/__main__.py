import argparse
from openai_commands.completion import NAME, VERSION
from openai_commands.completion.prompts.bash import bash_prompt
from openai_commands.logger import logger
from blueness.argparse.generic import ending


parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="pre_process_bash_description",
)
parser.add_argument(
    "--filename",
    type=str,
)
args = parser.parse_args()

success = False
if args.task == "pre_process_bash_description":
    success = bash_prompt.pre_process(args.filename)
else:
    success = None

ending(logger, NAME, args.task, success)
