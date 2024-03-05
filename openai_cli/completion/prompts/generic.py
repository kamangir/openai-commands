from typing import List


class ai_prompt:
    def __init__(self, objective: List[str]):
        self.objective = objective

    def create(
        self,
        function_name: str,
    ) -> str:
        return " ".join(self.objective).replace("{function_name}", function_name)
