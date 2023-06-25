from openai_cli.completion.functions.generic import ai_function


class ai_function_bash(ai_function):
    def __init__(self):
        super().__init__()
        self.language = "bash"
