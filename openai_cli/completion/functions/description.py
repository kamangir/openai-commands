import yaml
from abcli import file
from openai_cli.completion import NAME
from abcli import logging
import logging

logger = logging.getLogger(__name__)


def process_description(filename: str) -> bool:
    success, content = file.load_yaml(filename)
    if not success:
        return success

    return file.save_text(
        file.set_extension(filename, "txt"),
        [
            "to {}, run {}.".format(
                thing[1][:-1] if thing[1].endswith(".") else thing[1],
                thing[0],
            )
            .replace("\\n", "")
            .replace("\\t", "")
            .replace("\\", "")
            for thing in content
        ],
        log=True,
    )
