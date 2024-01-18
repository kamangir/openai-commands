import os
from abcli.modules.cookie import cookie

NAME = "openai_cli.images"

api_key = os.environ["OPENAI_API_KEY"] = cookie["openai_api_key"]
