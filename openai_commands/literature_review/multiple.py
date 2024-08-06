from blueness import module
from openai_commands import NAME
from openai_commands.logger import logger

NAME = module.name(__file__, NAME)


def generate_workflow(
    job_name: str,
    object_name: str,
    options: str,
    args: str,
    do_publish: bool = False,
    suffix: str = "",
) -> bool:
    if suffix == "-":
        suffix = ""

    logger.info(
        "{}.generate_workflow({}) {} -{}{}{}-> {}".format(
            NAME,
            job_name,
            object_name,
            options,
            "-publish" if do_publish else "",
            args.replace("\n", " | "),
            f"suffix={suffix}" if suffix else "",
        )
    )

    logger.info("🪄")

    return True
