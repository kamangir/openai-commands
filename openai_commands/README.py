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
        "thumbnail": "https://github.com/kamangir/assets/blob/main/openai_commands/literature-review/marquee.png?raw=true",
        "url": "./openai_commands/literature_review",
    },
    "prompt completion": {
        "thumbnail": default_thumbnail,
        "url": "./openai_commands/completion#%EF%B8%8F-prompt-completion",
    },
    "image generation": {
        "description": "sentence -> image, text -> mural, images",
        "thumbnail": "https://github.com/kamangir/openai-commands/blob/main/assets/DALL-E.png?raw=true",
        "url": "./openai_commands/images",
    },
    "vision": {
        "description": "a command interface to the [OpenAI vision API](https://platform.openai.com/docs/guides/vision).",
        "thumbnail": "https://raw.githubusercontent.com/kamangir/assets/main/vanwatch/2023-11-25-openai-vision/ButeNorthDavie.jpg",
        "url": "./openai_commands/vision",
    },
    "template": {
        "description": "",
        "thumbnail": default_thumbnail,
        "url": "",
    },
}


items = [
    "[`{}`]({}) [![image]({})]({}) {}".format(
        feature,
        details["url"],
        details["thumbnail"],
        details["url"],
        details.get("description", ""),
    )
    for feature, details in features.items()
    if feature != "template"
]


def build():
    return all(
        README.build(
            items=readme.get("items", []),
            cols=readme.get("cols", 3),
            path=os.path.join(file.path(__file__), readme["path"]),
            NAME=NAME,
            VERSION=VERSION,
            REPO_NAME=REPO_NAME,
        )
        for readme in [
            {
                "items": items,
                "path": "..",
            },
            {
                "items": literature_review_items,
                "cols": 2,
                "path": "literature_review",
            },
            {
                "path": "image_generation",
            },
        ]
    )
