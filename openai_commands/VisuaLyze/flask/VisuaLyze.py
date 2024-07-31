from flask import Flask, request
from blueness import module
from abcli import env
from openai_commands import env
from openai_commands import NAME, VERSION
from openai_commands.logger import logger
from openai_commands.VisuaLyze.order import VisuaLyzeOrder

NAME = module.name(__file__, NAME)

app = Flask(__name__)


@app.route("/")
def index():
    order = VisuaLyzeOrder(example_name="onlinefoods")
    return order.render()


@app.route("/VisuaLyze", methods=["POST"])
def process():
    order = VisuaLyzeOrder(
        prompt=request.form["prompt"].split("\n"),
        description=request.form["description"].split("\n"),
        data_filename=request.form["data_filename"],
        complete=True,
    )

    return order.render()


if __name__ == "__main__":
    logger.info(f"{NAME}.{VERSION} is running.")
    app.run(debug=True, port=env.VISUALYZE_PORT)
