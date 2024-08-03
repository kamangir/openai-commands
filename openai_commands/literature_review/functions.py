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
    log: bool = True,
) -> str:
    prompt = generate_prompt(abstract)
    success, assessment, _ = complete_prompt(prompt)
    assert success

    if log:
        logger.info(f"{assessment}: {abstract}")

    return assessment


def generate_prompt(abstract: str) -> str:
    prompt = f"""
        read this abstract of a scentific paper and return "antimicrobial" if it talks about antimicrobial 
        treatment for cholera. return "susceptibility" if it has information regarding antibiotic-reistance
        or susceptibility to cholerae strains. otherwise, return "not relevant". 

        {abstract}
        """

    prompt = prompt.replace("\n", " ")
    while "  " in prompt:
        prompt = prompt.replace("  ", " ")

    return prompt


def review_literature(
    object_name: str,
    filename: str,
    questions_filename: str,
    count: int,
) -> bool:
    logger.info(
        "{}.review_literature({}): {} -{}> {}".format(
            NAME,
            object_name,
            questions_filename,
            "" if count == -1 else f"{count}-",
            filename,
        )
    )

    success, df = file.load_dataframe(objects.path_of(filename, object_name), log=True)
    if not success:
        return success

    if count != -1:
        df = df.head(count)
    logger.info("processing {:,} item(s)...".format(len(df)))

    df["Screening Results"] = df["Abstract"].apply(assess_abstract)

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
