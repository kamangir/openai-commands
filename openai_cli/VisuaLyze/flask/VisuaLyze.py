from typing import List
from flask import Flask, render_template, request
from abcli.string.functions import pretty_date
from openai_cli import ICON
from openai_cli.VisuaLyze import NAME, VERSION
from openai_cli import env

app = Flask(__name__)

process_log: List[str] = []


@app.route("/")
def index():
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

    global process_log

    # TODO: process description

    process_log += [
        "{} - {} - {}".format(
            pretty_date(),
            data,
            description,
        )
    ]

    return render_template(
        "index.html",
        description=description,
        data=data,
        text="\n<hr />".join(process_log),
    )


if __name__ == "__main__":
    app.run(debug=True, port=env.VISUALYZE_PORT)
