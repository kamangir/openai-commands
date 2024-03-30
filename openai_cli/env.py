import os
from dotenv import load_dotenv

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(os.path.join(parent_dir, ".env"))
load_dotenv(os.path.join(parent_dir, "config.env"))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

OPENAI_CLI_VISION_TEST_OBJECT = os.getenv(
    "OPENAI_CLI_VISION_TEST_OBJECT",
    "",
)
OPENAI_CLI_FUNCTION_BASH_TEST_OBJECT = os.getenv(
    "OPENAI_CLI_FUNCTION_BASH_TEST_OBJECT",
    "",
)

VISUALYZE_PORT = os.getenv("VISUALYZE_PORT", "")

OPENAI_CLI_VISUALIZE_EXAMPLES_OBJECT = os.getenv(
    "OPENAI_CLI_VISUALIZE_EXAMPLES_OBJECT",
    "",
)

OPENAI_GPT_DEFAULT_MODEL = os.getenv("OPENAI_GPT_DEFAULT_MODEL", "")
