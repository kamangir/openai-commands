import os
from flask import Flask, render_template, request
from abcli import file
from abcli.string.functions import pretty_date
from abcli.env import abcli_path_git
from openai_cli import ICON
from abcli import env
from openai_cli.VisuaLyze import NAME, VERSION
from openai_cli import env
from openai_cli.logger import logger

app = Flask(__name__)


@app.route("/")
def index():
    success, description = file.load_text(
        os.path.join(
            abcli_path_git,
            "openai-cli/assets/VisuaLyze/descriptions.txt",
        ),
        log=True,
    )

    return render_template(
        "index.html",
        title=f"{NAME}.{VERSION}",
        h1=f"{ICON} {NAME}.{VERSION}",
        description=description,
        log="" if success else "⚠️ description not found.",
    )


@app.route("/VisuaLyze", methods=["POST"])
def process():
    description = request.form["description"]

    logger.info(f"VisuaLyzing {description}...")

    # TODO

    return render_template(
        "index.html",
        title=f"{NAME}.{VERSION}",
        h1=f"{ICON} {NAME}.{VERSION}",
        description=description,
        log=f"{pretty_date()}: {description}",
    )


if __name__ == "__main__":
    logger.info(f"{NAME}.{VERSION} is running.")
    app.run(debug=True, port=env.VISUALYZE_PORT)
