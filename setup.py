from openai_commands import NAME, VERSION, DESCRIPTION, REPO_NAME
from blueness.pypi import setup

setup(
    filename=__file__,
    repo_name=REPO_NAME,
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=[
        NAME,
        f"{NAME}.completion",
        f"{NAME}.completion.functions",
        f"{NAME}.completion.prompts",
        f"{NAME}.DALLE",
        f"{NAME}.gpt",
        f"{NAME}.images",
        f"{NAME}.literature_review",
        f"{NAME}.vision",
        f"{NAME}.VisuaLyze",
    ],
    include_package_data=True,
    package_data={
        NAME: [
            "config.env",
            "sample.env",
            ".abcli/**/*.sh",
        ],
    },
)
