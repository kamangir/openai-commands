import os
from abcli.env import load_env, load_config

load_env(__name__)
load_config(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

OPENAI_COMMANDS_VISION_TEST_OBJECT = os.getenv(
    "OPENAI_COMMANDS_VISION_TEST_OBJECT",
    "",
)
OPENAI_COMMANDS_FUNCTION_BASH_TEST_OBJECT = os.getenv(
    "OPENAI_COMMANDS_FUNCTION_BASH_TEST_OBJECT",
    "",
)

VISUALYZE_PORT = os.getenv("VISUALYZE_PORT", "")

OPENAI_GPT_DEFAULT_MODEL = os.getenv("OPENAI_GPT_DEFAULT_MODEL", "")
