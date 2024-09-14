from blue_objects import file, objects


class bash_prompt:
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

        return "\n".join(
            [
                (
                    line.replace(function_name, function_short_name)
                    if function_short_name
                    else line
                )
                for line in instructions + [self.prompt]
            ]
        )

    @staticmethod
    def pre_process(filename):
        success, content = file.load_yaml(filename)
        return (
            success
            if not success
            else file.save_text(
                file.add_extension(filename, "txt"),
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
        )
