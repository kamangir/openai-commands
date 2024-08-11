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
                "workflow monitor",
                f"node={question}",
                workflow.job_name,
                "literature_review",
                "question={},suffix={},{}".format(
                    question,
                    suffix,
                    review_options,
                ),
                object_name,
                args,
            ]
        )

        workflow.G.add_edge("combination", question)

    output_object_name = "-".join([object_name, suffix] + list_of_questions)

    workflow.G.nodes["combination"]["command_line"] = " ".join(
        [
            "workflow monitor",
            f"node=combination,publish_as={output_object_name}",
            workflow.job_name,
            "literature_review",
            "combine",
            "dryrun={},publish={}".format(
                int(do_dryrun),
                int(do_publish),
            ),
        ]
        + ["-".join([object_name, suffix, question]) for question in list_of_questions]
        + [output_object_name]
    )

    return workflow.save()
