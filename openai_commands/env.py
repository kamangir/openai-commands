import os
from blue_options.env import load_config, load_env

load_env(__name__)
load_config(__name__)

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY",
    "",
)

OPENAI_COMMANDS_VISION_TEST_OBJECT = os.getenv(
    "OPENAI_COMMANDS_VISION_TEST_OBJECT",
    "",
)
OPENAI_COMMANDS_FUNCTION_BASH_TEST_OBJECT = os.getenv(
    "OPENAI_COMMANDS_FUNCTION_BASH_TEST_OBJECT",
    "",
)

VISUALYZE_PORT = os.getenv(
    "VISUALYZE_PORT",
    "",
)

OPENAI_GPT_DEFAULT_MODEL = os.getenv(
    "OPENAI_GPT_DEFAULT_MODEL",
    "",
)

LITERATURE_REVIEW_OBJECT = os.getenv(
    "LITERATURE_REVIEW_OBJECT",
    "",
)
LITERATURE_REVIEW_TEST_FILENAME = os.getenv(
    "LITERATURE_REVIEW_TEST_FILENAME",
    "",
)
LITERATURE_REVIEW_TEST_QUESTION = os.getenv(
    "LITERATURE_REVIEW_TEST_QUESTION",
    "",
)
