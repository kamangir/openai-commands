from abcli import file
from abcli.modules import objects


class bash_prompt(object):
    def __init__(self, prompt: str):
        self.prompt = prompt

    def create(
        self,
        function_name: str,
        function_short_name: str,
    ) -> str:
        success, instructions = file.load_text(
            objects.path_of(f"{function_short_name}-description.txt"),
            log=True,
        )
        assert success

        return [
            line.replace(function_name, function_short_name)
            if function_short_name
            else line
            for line in instructions + [self.prompt]
        ]
