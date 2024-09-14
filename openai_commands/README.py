import os

from blue_objects import file, README

from openai_commands.literature_review.README import items as literature_review_items
from openai_commands import NAME, VERSION, ICON, REPO_NAME


default_thumbnail = (
    "https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true"
)

features = {
    "literature review": {
        "description": "literature review using OpenAI API.",
        "icon": ICON,
        "thumbnail": "https://github.com/kamangir/assets/blob/main/openai_commands/literature-review/marquee.png?raw=true",
        "url": "https://github.com/kamangir/openai-commands/tree/main/openai_commands/literature_review",
    },
    "OpenAI Vision API": {
        "description": "a command interface to the [OpenAI vision API](https://platform.openai.com/docs/guides/vision).",
        "icon": ICON,
        "thumbnail": "https://raw.githubusercontent.com/kamangir/assets/main/vanwatch/2023-11-25-openai-vision/ButeNorthDavie.jpg",
        "url": "https://github.com/kamangir/openai-commands/tree/main/openai_commands/vision",
    },
    "code generation": {
        "description": "example notebooks to [generate python functions](./notebooks/completion_ai_function_py.ipynb), special case for [image to image python functions](./notebooks/completion_i2i_function.ipynb), and to [write a bash script](./notebooks/completion_ai_function_bash.ipynb) to use a script, for example, [vancouver-watching](https://github.com/kamangir/vancouver-watching).",
        "icon": ICON,
        "thumbnail": "https://github.com/kamangir/openai-commands/blob/main/assets/completion_i2i_function.png?raw=true",
        "url": "https://github.com/kamangir/openai-commands/tree/main/openai_commands/completion#%EF%B8%8F-code-generation",
    },
    "gpt": {
        "description": "co-authored with ChapGPT.",
        "icon": ICON,
        "thumbnail": default_thumbnail,
        "url": "https://github.com/kamangir/openai-commands/tree/main/openai_commands/gpt",
    },
    "VisuaLyze": {
        "description": 'How about calling it "VisuaLyze"? This name combines "visualize" and "analyze," reflecting the tool\'s capability to generate custom data visualizations and analyze user input through AI - OpenAI',
        "icon": ICON,
        "thumbnail": "https://github.com/kamangir/openai-commands/assets/1007567/7c0ed5f7-6941-451c-a17e-504c6adab23f",
        "url": "https://github.com/kamangir/openai-commands/tree/main/openai_commands/VisuaLyze",
    },
    "prompt completion": {
        "description": "basic prompt completion.",
        "icon": ICON,
        "thumbnail": default_thumbnail,
        "url": "https://github.com/kamangir/openai-commands/tree/main/openai_commands/completion#%EF%B8%8F-prompt-completion",
    },
    "image generation": {
        "description": "sentence -> image, text -> mural, images",
        "icon": ICON,
        "thumbnail": "https://github.com/kamangir/openai-commands/blob/main/assets/DALL-E.png?raw=true",
        "url": "https://github.com/kamangir/openai-commands/tree/main/openai_commands/images",
    },
    "template": {
        "description": "",
        "icon": ICON,
        "thumbnail": default_thumbnail,
        "url": "",
    },
}


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


def build():
    return README.build(
        items=items,
        path=os.path.join(file.path(__file__), ".."),
        NAME=NAME,
        VERSION=VERSION,
        REPO_NAME=REPO_NAME,
    ) and README.build(
        items=literature_review_items,
        cols=2,
        path=os.path.join(file.path(__file__), "literature_review"),
        NAME=NAME,
        VERSION=VERSION,
        REPO_NAME=REPO_NAME,
    )
