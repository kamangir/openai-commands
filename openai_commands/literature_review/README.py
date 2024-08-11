from functools import reduce
from abcli import string


prefix = "https://kamangir-public.s3.ca-central-1.amazonaws.com"
runner_prefix = "https://github.com/kamangir/notebooks-and-scripts/tree/main/notebooks_and_scripts/workflow/runners"

list_of_runners = ["aws_batch", "local"]

items = [
    f"[{runner_type}]({runner_prefix}/{runner_type}.py)"
    for runner_type in list_of_runners
] + [
    f"[![image]({url})]({url})"
    for url in [
        "{}/AMR-v7-test-litrev-multiple-{}-study-type-screening-result/workflow.gif?raw=true&random={}".format(
            prefix,
            runner_type,
            string.random_(),
        )
        for runner_type in list_of_runners
    ]
]
