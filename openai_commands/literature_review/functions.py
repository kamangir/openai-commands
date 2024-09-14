from typing import Dict
import re
import pandas as pd
from tqdm import tqdm

from blueness import module
from blue_objects import file, objects

from openai_commands import NAME
from openai_commands.completion.api import complete_prompt
from openai_commands.logger import logger


NAME = module.name(__file__, NAME)


def clean_prompt(prompt):
    return re.sub(r"\s+", " ", prompt.strip())


def generate_prompt(question: Dict[str, Dict]) -> str:
    choices = question.get("choices", {})
    description = question.get(
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

    prompt = """
    {} and return the correct choice from the following list followed with "because" and 
    then describe the reason for this choice in less than ten words. choices: {}
    """.format(
        description,
        " ".join(
            [
                f'"{choice}" {description}'
                for choice, description in choices.items()
                if choice != "otherwise"
            ]
            + ['"not relevant" if none of the above choices is correct."']
        ),
    )

    prompt = clean_prompt(prompt)

    logger.info(f"prompt: {prompt}")
    return prompt


def review_literature(
    input_object_name: str,
    output_object_name: str,
    filename: str,
    question: str,
    count: int,
    overwrite: bool = False,
    verbose: bool = False,
) -> bool:
    if filename.endswith(".csv"):
        filename = filename.split(".csv")[0]

    logger.info(
        "{}.review_literature: {}/{}.csv -{}-{}{}> {}/{}-{}.csv[{}]".format(
            NAME,
            input_object_name,
            filename,
            question,
            "" if count == -1 else f"{count}X-",
            "" if not overwrite else "overwrite-",
            output_object_name,
            filename,
            question,
            question,
        )
    )

    success, question_dict = file.load_yaml(
        objects.path_of(f"{question}.yaml", input_object_name)
    )
    if not success:
        return success

    output_filename = objects.path_of(
        f"{filename}.csv",
        output_object_name,
        create=True,
    )
    input_filename = objects.path_of(
        f"{filename}.csv",
        input_object_name,
    )
    if not overwrite and file.exists(output_filename):
        logger.info(
            "continuing from a previous run: {} ...".format(file.name(output_filename))
        )
        input_filename = output_filename

    success, df = file.load_dataframe(input_filename, log=True)
    if not success:
        return success

    prompt = generate_prompt(question_dict)

    if question not in df.columns:
        df[question] = pd.NA
        logger.info("added column: {}".format(question))

    counter = 0
    for idx in tqdm(df.index):
        assessment = df.loc[idx, question]
        if (
            not overwrite
            and not pd.isna(assessment)
            and assessment != ""
            and not assessment.startswith("failure")
        ):
            logger.info(f"✅ {assessment}")
            continue

        abstract = str(df.loc[idx, "Abstract"])

        success, assessment, _ = complete_prompt(
            clean_prompt(f"{prompt} {abstract}"),
            verbose=verbose,
        )
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

        df.loc[idx, question] = assessment

        counter += 1
        if count != -1 and counter >= count:
            break
    logger.info(f"processed {counter:,} item(s)")

    return file.save_csv(
        output_filename,
        df,
        log=True,
    )
