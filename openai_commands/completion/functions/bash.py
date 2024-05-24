from typing import Tuple, Dict, Any
from openai_commands.completion.functions.generic import ai_function


class ai_function_bash(ai_function):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "bash"
