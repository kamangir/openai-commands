from flask import Flask, request
from abcli import env
from openai_cli import env
from openai_cli.logger import logger
from openai_cli.VisuaLyze import NAME, VERSION
from openai_cli.VisuaLyze.order import VisuaLyzeOrder

app = Flask(__name__)


@app.route("/")
def index():
    order = VisuaLyzeOrder(example_name="onlinefoods")
    return order.render()


@app.route("/VisuaLyze", methods=["POST"])
def process():
    order = VisuaLyzeOrder(
        prompt=request.form["prompt"],
        description=request.form["description"].split("\n"),
        data_filename=request.form["data_filename"],
        object_name=request.form["object_name"],
    )

    order.load_data()

    order.complete()

    return order.render()


if __name__ == "__main__":
    logger.info(f"{NAME}.{VERSION} is running.")
    app.run(debug=True, port=env.VISUALYZE_PORT)
