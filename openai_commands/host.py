from typing import List

from abcli.host import signature as abcli_signature
from blueflow import fullname as blueflow_fullname

from openai_commands import fullname


def signature() -> List[str]:
    return [
        fullname(),
        blueflow_fullname(),
    ] + abcli_signature()
