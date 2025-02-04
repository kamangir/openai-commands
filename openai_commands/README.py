import os

from blue_objects import file, README

from openai_commands.literature_review.README import items as literature_review_items
from openai_commands import NAME, VERSION, ICON, REPO_NAME


default_thumbnail = (
    "https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true"
)

features = {
    "AI DAG runner": {
        "thumbnail": "https://github.com/kamangir/assets/raw/main/blue-amo-2025-02-03-nswnx6/stitching_the_frames-2.png?raw=true",
        "url": "https://github.com/kamangir/blue-assistant",
    },
    "literature review": {
        "thumbnail": "https://github.com/kamangir/assets/blob/main/openai_commands/literature-review/marquee.png?raw=true",
        "url": "./openai_commands/literature_review",
    },
    "text generation": {
        "thumbnail": default_thumbnail,
        "url": "./openai_commands/text_generation",
    },
    "image generation": {
        "thumbnail": "https://github.com/kamangir/openai-commands/blob/main/assets/DALL-E.png?raw=true",
        "url": "./openai_commands/images",
    },
    "vision": {
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
                "cols": 3,
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
