from typing import Dict
import re
import pandas as pd
from blueness import module
from abcli import file
from abcli.modules import objects
from openai_commands import NAME
from openai_commands.completion.api import complete_prompt
from openai_commands.logger import logger
from tqdm import tqdm


NAME = module.name(__file__, NAME)


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

    prompt = '{} and {} otherwise, return "{}" followed by reason in less than five words.'.format(
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
    suffix: str = "",
    overwrite: bool = False,
    verbose: bool = False,
) -> bool:
    if not suffix:
        suffix = file.name(choices_filename)

    logger.info(
        "{}.review_literature: {}/{} -{}-{}{}> {}".format(
            NAME,
            object_name,
            filename,
            choices_filename,
            "" if count == -1 else f"{count}X-",
            "" if not overwrite else "overwrite-",
            suffix,
        )
    )

    success, instructions = file.load_yaml(
        objects.path_of(choices_filename, object_name)
    )
    if not success:
        return success

    output_filename = objects.path_of(
        file.add_postfix(filename, suffix),
        object_name,
    )
    input_filename = objects.path_of(filename, object_name)
    if not overwrite and file.exist(output_filename):
        logger.info(
            "continuing from a previous run: {} ...".format(file.name(output_filename))
        )
        input_filename = output_filename

    success, df = file.load_dataframe(input_filename, log=True)
    if not success:
        return success

    prompt = generate_prompt(instructions)

    if suffix not in df.columns:
        df[suffix] = pd.NA
        logger.info("added column: {}".format(suffix))

    counter = 0
    for idx in tqdm(df.index):
        assessment = df.loc[idx, suffix]
        if not overwrite and not pd.isna(assessment) and assessment != "":
            logger.info(f"✅ {assessment}")
            continue

        abstract = df.loc[idx, "Abstract"]

        prompt = clean_prompt(f"{prompt} {abstract}")

        success, assessment, _ = complete_prompt(prompt, verbose=verbose)
        if not success:
            assessment = f"failure: {assessment}"

        logger.info(
            " | ".join(
                [assessment]
                + (
                    [abstract]
                    if verbose
                    else [
                        "{} ... ".format(abstract[:100]),
                    ]
                )
            )
        )

        df.loc[idx, suffix] = assessment

        counter += 1
        if count != -1 and counter >= count:
            break
    logger.info(f"processed {counter:,} item(s)")

    return file.save_csv(
        output_filename,
        df,
        log=True,
    )
