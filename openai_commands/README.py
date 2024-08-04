import os
from blueness import module
import abcli
from abcli import file
from abcli.file.functions import build_from_template
from abcli.plugins import markdown
from openai_commands import NAME, VERSION, ICON
from openai_commands.logger import logger

NAME = module.name(__file__, NAME)

default_thumbnail = (
    "https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true"
)

features = {
    "prompt completion": {
        "description": "basic prompt completion.",
        "icon": ICON,
        "thumbnail": default_thumbnail,
        "url": "https://github.com/kamangir/openai-commands/tree/main/openai_commands/completion#%EF%B8%8F-prompt-completion",
    },
    "code generation": {
        "description": "example notebooks to [generate python functions](./notebooks/completion_ai_function_py.ipynb), special case for [image to image python functions](./notebooks/completion_i2i_function.ipynb), and to [write a bash script](./notebooks/completion_ai_function_bash.ipynb) to use a script, for example, [vancouver-watching](https://github.com/kamangir/vancouver-watching).",
        "icon": ICON,
        "thumbnail": "https://github.com/kamangir/openai-commands/blob/main/assets/completion_i2i_function.png?raw=true",
        "url": "https://github.com/kamangir/openai-commands/tree/main/openai_commands/completion#%EF%B8%8F-code-generation",
    },
    "VisuaLyze": {
        "description": 'How about calling it "VisuaLyze"? This name combines "visualize" and "analyze," reflecting the tool\'s capability to generate custom data visualizations and analyze user input through AI - OpenAI',
        "icon": ICON,
        "thumbnail": "https://github.com/kamangir/openai-commands/assets/1007567/7c0ed5f7-6941-451c-a17e-504c6adab23f",
        "url": "https://github.com/kamangir/openai-commands/tree/main/openai_commands/VisuaLyze",
    },
    "gpt": {
        "description": "co-authored with ChapGPT.",
        "icon": ICON,
        "thumbnail": default_thumbnail,
        "url": "https://github.com/kamangir/openai-commands/tree/main/openai_commands/gpt",
    },
    "OpenAI Vision API": {
        "description": "implements the [OpenAI vision API](https://platform.openai.com/docs/guides/vision).",
        "icon": ICON,
        "thumbnail": "https://raw.githubusercontent.com/kamangir/assets/main/vanwatch/2023-11-25-openai-vision/ButeNorthDavie.jpg",
        "url": "https://github.com/kamangir/openai-commands/tree/main/openai_commands/vision",
    },
    "image generation": {
        "description": "sentence -> image, text -> mural, images",
        "icon": ICON,
        "thumbnail": "https://github.com/kamangir/openai-commands/blob/main/assets/DALL-E.png?raw=true",
        "url": "https://github.com/kamangir/openai-commands/tree/main/openai_commands/images",
    },
    "literature review": {
        "description": "literature review using OpenAI API.",
        "icon": ICON,
        "thumbnail": "https://github.com/kamangir/assets/blob/main/openai_commands/literature-review/marquee.png?raw=true",
        "url": "https://github.com/kamangir/openai-commands/tree/main/openai_commands/literature_review",
    },
    "template": {
        "description": "",
        "icon": ICON,
        "thumbnail": default_thumbnail,
        "url": "",
    },
}


def build(filename: str = ""):
    if not filename:
        filename = os.path.join(file.path(__file__), "../README.md")

    logger.info(f"{NAME}.build: {filename}")

    items = [
        "{}[`{}`]({}) [![image]({})]({}) {}".format(
            details["icon"],
            feature,
            details["url"],
            details["thumbnail"],
            details["url"],
            details["description"],
        )
        for feature, details in features.items()
        if feature != "template"
    ]

    table = markdown.generate_table(items, cols=3)

    signature = [
        "---",
        "built by [`{}`]({}), based on [`{}-{}`]({}).".format(
            abcli.fullname(),
            "https://github.com/kamangir/awesome-bash-cli",
            NAME,
            VERSION,
            "https://github.com/kamangir/openai-commands",
        ),
    ]

    return file.build_from_template(
        os.path.join(file.path(__file__), "./assets/README.md"),
        {
            "--table--": table,
            "--signature": signature,
        },
        filename,
    )
