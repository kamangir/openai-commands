import os
import pandas as pd
from typing import List
from flask import render_template

from blueness import module
from blue_options import string
from blue_objects import file

from openai_commands import ICON, NAME, VERSION
from openai_commands import env
from openai_commands.gpt.chat import interact_with_openai
from openai_commands.logger import logger

NAME = module.name(__file__, NAME)

examples_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../assets/VisuaLyze")
)


class VisuaLyzeOrder:
    def __init__(
        self,
        example_name: str = "",
        prompt: List[str] = [],
        description: List[str] = [],
        data_filename: str = "",
        load_data: bool = True,
        complete: bool = False,
        log: bool = True,
        model_name: str = env.OPENAI_GPT_DEFAULT_MODEL,
    ):
        self.prompt: List[str] = prompt
        self.description: List[str] = description
        self.data_filename: str = data_filename
        self.df = pd.DataFrame()

        self.source_code: List[str] = []

        self.valid: bool = True

        if example_name:
            if not self.load_example(
                name=example_name,
                load_data=False,
                log=log,
            ):
                self.valid = False

        if load_data and self.valid:
            if not self.load_data(log=log):
                self.valid = False

        if complete and self.valid:
            if not self.complete(model_name=model_name):
                self.valid = False

        if log:
            logger.info(self.one_liner())

    def complete(
        self,
        model_name: str = env.OPENAI_GPT_DEFAULT_MODEL,
        output_path: str = "",
    ) -> bool:
        success, self.source_code = interact_with_openai(
            prompt=self.full_prompt,
            output_path=output_path,
            model_name=model_name,
        )
        if not success:
            self.valid = False
        return success

    @property
    def full_prompt(self):
        return f"{self.prompt}. {self.description}"

    def load_data(
        self,
        log: bool = True,
    ) -> bool:
        success, self.df = file.load_dataframe(
            filename=self.data_filename,
            log=log,
        )
        if not success:
            self.valid = False
        return success

    def load_example(
        self,
        name: str = "onlinefoods",
        load_data: bool = True,
        log: bool = True,
    ) -> bool:
        success, examples = file.load_yaml(os.path.join(examples_path, "examples.yaml"))
        if not success:
            return success

        path = os.path.join(examples_path, name)

        try:
            example = [example for example in examples if example["name"] == name][0]

            success, self.prompt = file.load_text(
                os.path.join(path, "prompt.txt"),
                log=log,
            )
            assert success

            success, self.description = file.load_text(
                os.path.join(path, "description.txt"),
                log=log,
            )
            assert success

            self.data_filename = os.path.join(path, "data.csv")

        except Exception as e:
            logger.error(f"failed to load example {name}: {e}.")
            return False

        return self.load_data(log=log) if load_data else True

    def one_liner(self):
        return "{} {}: {} {}: {} - {} row(s) of {}: {}".format(
            "📜 valid" if self.valid else "⚠️ invalid",
            self.__class__.__name__,
            " ".join(self.prompt),
            " ".join(self.description),
            self.data_filename,
            len(self.df),
            ", ".join(self.df.columns),
            " ".join(self.source_code),
        )

    def render(self, status: str = ""):
        return render_template(
            "index.html",
            title=f"{NAME}.{VERSION}",
            h1=f"{ICON} {NAME}.{VERSION}",
            prompt="\n".join(self.prompt),
            description="\n".join(self.description),
            data_filename=self.data_filename,
            timestamp=string.pretty_date(),
            github_url="https://github.com/kamangir/openai-commands/tree/main/openai_commands/VisuaLyze",
            dataframe_html=self.df.head().to_html(),
            status="{}{}".format(
                (
                    "<pre><code>{}</code></pre>".format("\n".join(self.source_code))
                    if self.source_code
                    else ""
                ),
                f", {status}" if status else "",
            ),
        )
