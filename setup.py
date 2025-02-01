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
        f"{NAME}.help",
        f"{NAME}.image_generation",
        f"{NAME}.literature_review",
        f"{NAME}.prompt_completion",
        f"{NAME}.vision",
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
