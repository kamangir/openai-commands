from typing import Tuple, Dict, Any
from abcli import file
from abcli.modules import objects
from openai_cli.completion.functions.generic import ai_function


class ai_function_bash(ai_function):
    def __init__(
        self,
        *args,
        function_short_name: str = "",
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.language = "bash"
        self.function_short_name = function_short_name

        self.instructions = file.load_text(
            objects.path_of(f"{self.function_short_name}-description.txt"),
            log=True,
        )[1]

    def generate(
        self,
        prompt,
    ) -> Tuple[bool, Dict[str, Any]]:
        return super().generate(
            [
                line.replace(self.function_name, self.function_short_name)
                if self.function_short_name
                else line
                for line in self.instructions + [prompt]
            ]
        )
