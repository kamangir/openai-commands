from openai_commands import NAME, VERSION, DESCRIPTION, ICON
from openai_commands.logger import logger
from openai_commands import README
from blueness.argparse.generic import main

success, message = main(
    __file__,
    NAME,
    VERSION,
    DESCRIPTION,
    ICON,
    {
        "build_README": lambda _: README.build(),
    },
)
if not success:
    logger.error(message)
