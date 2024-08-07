from typing import List
from blueness import module
from notebooks_and_scripts.workflow.generic import Workflow
from openai_commands import NAME
from openai_commands.logger import logger

NAME = module.name(__file__, NAME)


def generate_workflow(
    job_name: str,
    object_name: str,
    list_of_questions: List[str],
    review_options: str,
    args: str,
    do_publish: bool = False,
    suffix: str = "",
    do_dryrun: bool = False,
) -> bool:
    if suffix == "-":
        suffix = ""

    logger.info(
        "{}.generate_workflow({}) {} -{}{}{}{}-> {}".format(
            NAME,
            job_name,
            object_name,
            review_options,
            "-{} question(s): {}".format(
                len(list_of_questions),
                ", ".join(list_of_questions),
            ),
            "-publish" if do_publish else "",
            args.replace("\n", " | "),
            f"suffix={suffix}" if suffix else "",
        )
    )

    workflow = Workflow(job_name)

    workflow.G.add_node("combination")

    for question in list_of_questions:
        workflow.G.add_node(question)
        workflow.G.nodes[question]["command_line"] = " ".join(
            [
                "literature_review",
                f"{review_options},question={question},suffix={suffix}",
                object_name,
                args,
            ]
        )

        workflow.G.add_edge("combination", question)

    workflow.G.nodes[question]["command_line"] = " ".join(
        [
            "literature_review",
            "combine",
            f"dryrun={do_dryrun},publish={do_publish}",
        ]
        + [f"{object_name}-{question}{suffix}" for question in list_of_questions]
        + "{}-{}{}".format(
            object_name,
            "-".join(list_of_questions),
            suffix,
        )
    )

    return workflow.save()