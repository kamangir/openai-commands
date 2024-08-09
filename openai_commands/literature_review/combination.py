from blueness import module
from openai_commands import NAME
from openai_commands.logger import logger

NAME = module.name(__file__, NAME)


def combine(
    object_name_1: str,
    object_name_2: str,
    object_name: str,
) -> bool:
    logger.info(
        "{}.combine: {} + {} -> {}".format(
            NAME,
            object_name_1,
            object_name_2,
            object_name,
        )
    )

    logger.info("🪄")

    return True
