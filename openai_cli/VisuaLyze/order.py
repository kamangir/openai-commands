import os
import pandas as pd
from typing import List
from flask import render_template
from abcli import file
from abcli import string
from abcli.modules.objects import path_of, object_path
from openai_cli import ICON
from openai_cli import env
from openai_cli.gpt.chat import interact_with_openai
from openai_cli.VisuaLyze import NAME, VERSION
from openai_cli.logger import logger

examples_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../assets/VisuaLyze")
)


class VisuaLyzeOrder:
    def __init__(
        self,
        example_name: str = "",
        prompt: str = "",
        description: List[str] = [],
        data_filename: str = "",
        object_name: str = env.OPENAI_CLI_VISUALIZE_EXAMPLES_OBJECT,
        load: bool = True,
        log: bool = True,
    ):
        self.prompt: str = prompt
        self.description: List[str] = description
        self.object_name: str = object_name
        self.data_filename: str = data_filename
        self.df = pd.DataFrame()

        self.source_code = List[str]

        self.valid: bool = True

        if example_name and not self.load_example(
            name=example_name,
            load=False,
            log=log,
        ):
            self.valid = False

        if load and not self.load_data(log=log):
            self.valid = False

        if log:
            logger.info(self.one_liner())

    def complete(
        self,
        model_name: str = env.OPENAI_GPT_DEFAULT_MODEL,
    ) -> bool:
        success, self.source_code = interact_with_openai(
            prompt=self.full_prompt,
            object_path=object_path(object_name=self.object_name),
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
            path_of(
                filename=self.data_filename,
                object_name=self.object_name,
            ),
            log=log,
        )
        if not success:
            self.valid = False
        return success

    def load_example(
        self,
        name: str = "onlinefoods",
        load: bool = True,
        log: bool = True,
    ) -> bool:
        success, examples = file.load_yaml(os.path.join(examples_path, "examples.yaml"))
        if not success:
            return success

        try:
            example = [example for example in examples if example["name"] == name][0]

            self.prompt = example["prompt"]

            success, self.description = file.load_text(
                path_of(
                    filename=example["description"],
                    object_name=example["object_name"],
                ),
                log=log,
            )
            assert success

            self.object_name = example["object_name"]
            self.data_filename = example["data"]

        except Exception as e:
            logger.error(f"failed to load example {name}: {e}.")
            return False

        return not load or self.load_data(log=log)

    def one_liner(self):
        return "{} {}: {} {}: {}/{} - {} row(s) of {}".format(
            "📜 valid" if self.valid else "⚠️ invalid",
            self.__class__.__name__,
            self.prompt,
            " ".join(self.description),
            self.object_name,
            self.data_filename,
            len(self.df),
            ", ".join(self.df.columns),
        )

    def render(self, status: str = ""):
        return render_template(
            "index.html",
            title=f"{NAME}.{VERSION}",
            h1=f"{ICON} {NAME}.{VERSION}",
            prompt=self.prompt,
            description="\n".join(self.description),
            data_filename=self.data_filename,
            object_name=self.object_name,
            status="{}{}".format(
                self.one_liner(),
                f", {status}" if status else "",
            ),
            timestamp=string.pretty_date(),
            github_url="https://github.com/kamangir/openai-cli/tree/main/openai_cli/VisuaLyze",
            dataframe_html=self.df.to_html(),
        )
