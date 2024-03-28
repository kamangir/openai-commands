from flask import Flask, render_template
from openai_cli import ICON
from openai_cli.VisuaLyze import NAME, VERSION
from openai_cli import env

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        title=f"{NAME}.{VERSION}",
        h1=f"{ICON} {NAME}.{VERSION}",
        text="wip 🚧",
    )


if __name__ == "__main__":
    app.run(debug=True, port=env.VISUALYZE_PORT)
