from openai_commands import NAME, VERSION, DESCRIPTION, ICON
from openai_commands.logger import logger
from openai_commands import README
from blueness.argparse.generic import main

main(
    ICON=ICON,
    NAME=NAME,
    DESCRIPTION=DESCRIPTION,
    VERSION=VERSION,
    main_filename=__file__,
    tasks={
        "build_README": lambda _: README.build(),
    },
    logger=logger,
)
