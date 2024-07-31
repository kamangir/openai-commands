from blueness import module
from openai_commands import NAME
from openai_commands.logger import logger


NAME = module.name(__file__, NAME)


def review_literature(
    object_name: str,
    filename: str,
    questions: str,
    count: int,
) -> bool:
    logger.info(
        "{}.review_literature({}): {} -{}> {}".format(
            NAME,
            object_name,
            questions,
            "" if count == -1 else f"{count}-",
            filename,
        )
    )

    logger.info("🪄")

    return True
