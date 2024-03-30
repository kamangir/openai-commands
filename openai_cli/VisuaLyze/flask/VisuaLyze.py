import os
from flask import Flask, render_template, request
from abcli import file
from abcli.string.functions import pretty_date
from openai_cli import ICON
from abcli import env
from openai_cli.VisuaLyze import NAME, VERSION
from openai_cli.VisuaLyze.order import VisuaLyzeOrder
from openai_cli import env
from openai_cli.logger import logger

app = Flask(__name__)


@app.route("/")
def index():
    order = VisuaLyzeOrder(example_name="onlinefoods")
    return order.render()


@app.route("/VisuaLyze", methods=["POST"])
def process():
    order = VisuaLyzeOrder(
        prompt=request.form["prompt"],
        description=request.form["description"],
        data_filename=request.form["data_filename"],
        object_name=request.form["object_name"],
    )

    order.load_data()

    return order.render()


if __name__ == "__main__":
    logger.info(f"{NAME}.{VERSION} is running.")
    app.run(debug=True, port=env.VISUALYZE_PORT)
