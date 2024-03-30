import os
import pandas as pd
from typing import List
from flask import render_template
from abcli import file
from openai_cli import ICON
from openai_cli.VisuaLyze import NAME, VERSION
from openai_cli.logger import logger

examples_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../assets/VisuaLyze")
)


class VisuaLyzeOrder:
    def __init__(
        self,
        prompt: str = "",
        description: str = "",
        data: str = "",
        name: str = "",
        load: bool = False,
        log: bool = False,
    ):
        self.prompt: str = prompt
        self.description: List[str] = description.split(",")
        self.data_filename: str = data
        self.df = pd.DataFrame()

        self.valid: bool = True

        if name and not self.load_example(name=name, load=load):
            self.valid = False

        if load and not self.load_data():
            self.valid = False

        if log:
            self.log()

    @staticmethod
    def example_filename(filename: str) -> str:
        return os.path.abspath(os.path.join(examples_path, filename))

    def load_data(self) -> bool:
        success, self.df = file.load_dataframe(self.data_filename, log=True)
        if not success:
            self.valid = False
        return success

    def load_example(
        self,
        name: str = "onlinefoods",
        load: bool = False,
    ) -> bool:
        success, examples = file.load_yaml(os.path.join(examples_path, "examples.yaml"))
        if not success:
            return success

        try:
            example = [example for example in examples if example["name"] == name][0]

            self.prompt = example["prompt"]

            success, self.description = file.load_text(
                self.example_filename(example["description"])
            )
            assert success

            self.data_filename = self.example_filename(example["data"])
        except Exception as e:
            logger.error(f"failed to load example {name}: {e}.")
            return False

        return not load or self.load_data()

    def render(self, log: str = ""):
        return render_template(
            "index.html",
            title=f"{NAME}.{VERSION}",
            h1=f"{ICON} {NAME}.{VERSION}",
            prompt=self.prompt,
            description="\n".join(self.description),
            filename=self.data_filename,
            log=(
                log
                if self.valid
                else "⚠️ invalid order{}".format(f", {log}" if log else "")
            ),
        )
