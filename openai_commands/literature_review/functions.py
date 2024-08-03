from typing import Dict
import re
from blueness import module
from abcli import file
from abcli import string
from abcli.modules import objects
from openai_commands import NAME
from openai_commands.completion.api import complete_prompt
from openai_commands.logger import logger


NAME = module.name(__file__, NAME)


def assess_abstract(
    abstract: str,
    prompt: str,
    log: bool = True,
) -> str:
    prompt = clean_prompt(f"{prompt} {abstract}")

    success, assessment, _ = complete_prompt(prompt)
    assert success

    if log:
        logger.info(f"{assessment}: {abstract}")

    return assessment


def clean_prompt(prompt):
    return re.sub("\s+", " ", prompt.strip())


def generate_prompt(instructions: Dict[str, Dict]) -> str:
    choices = instructions.get("choices", {})
    description = instructions.get(
        "description",
        "read this abstract of a scentific paper",
    )

    logger.info(
        "{} @ {} choice(s): {}".format(
            description,
            len(choices),
            choices,
        )
    )

    prompt = '{} and {} otherwise, return "{}".'.format(
        description,
        " ".join(
            [
                f'return "{choice}" {description}'
                for choice, description in choices.items()
                if choice != "otherwise"
            ]
        ),
        choices.get("otherwise", "not relevant"),
    )

    prompt = clean_prompt(prompt)

    logger.info(f"prompt: {prompt}")
    return prompt


def review_literature(
    object_name: str,
    filename: str,
    choices_filename: str,
    count: int,
) -> bool:
    logger.info(
        "{}.review_literature({}): {} -{}> {}".format(
            NAME,
            object_name,
            choices_filename,
            "" if count == -1 else f"{count}-",
            filename,
        )
    )

    success, instructions = file.load_yaml(
        objects.path_of(
            choices_filename,
            object_name,
        )
    )
    if not success:
        return success

    success, df = file.load_dataframe(
        objects.path_of(
            filename,
            object_name,
        ),
        log=True,
    )
    if not success:
        return success

    if count != -1:
        df = df.head(count)
    logger.info("processing {:,} item(s)...".format(len(df)))

    prompt = generate_prompt(instructions)

    df["Screening Results"] = df["Abstract"].apply(
        lambda abstract: assess_abstract(
            abstract=abstract,
            prompt=prompt,
            log=True,
        )
    )

    return file.save_csv(
        objects.path_of(
            file.add_postfix(
                filename,
                "screening-results-{}".format(
                    string.pretty_date(
                        date=None,
                        as_filename=True,
                        unique=True,
                    )
                ),
            ),
            object_name,
        ),
        df,
        log=True,
    )
