import os
from abcli.modules.cookie import cookie

NAME = "openai_cli"

VERSION = "2.227.1"

DESCRIPTION = "🛠️ tools for the OpenAI API"


api_key = os.environ["OPENAI_API_KEY"] = cookie["openai_api_key"]
