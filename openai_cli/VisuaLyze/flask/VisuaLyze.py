from typing import List
from flask import Flask, render_template, request
from abcli.string.functions import pretty_date
from openai_cli import ICON
from openai_cli.VisuaLyze import NAME, VERSION
from openai_cli import env
from openai_cli.logger import logger

app = Flask(__name__)


@app.route("/")
def index():
    logger.info("root")

    return render_template(
        "index.html",
        title=f"{NAME}.{VERSION}",
        h1=f"{ICON} {NAME}.{VERSION}",
        description="visualize this data.",
        data="🚧",
        text="",
    )


@app.route("/process", methods=["POST"])
def process():
    description = request.form["description"]
    data = request.form["data"]

    # TODO: process description

    message = "{} - {}: {}".format(
        pretty_date(),
        description,
        data,
    )
    logger.info(message)

    return render_template(
        "index.html",
        title=f"{NAME}.{VERSION}",
        h1=f"{ICON} {NAME}.{VERSION}",
        description=description,
        data=data,
        text=message,
    )


if __name__ == "__main__":
    logger.info(f"{NAME}.{VERSION} is running.")
    app.run(debug=True, port=env.VISUALYZE_PORT)
