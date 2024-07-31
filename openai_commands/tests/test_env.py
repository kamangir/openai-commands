from abcli.tests import test_env
from openai_commands import env


def test_abcli_env():
    test_env.test_abcli_env()


def test_openai_commands_env():
    assert env.OPENAI_API_KEY
    assert env.OPENAI_COMMANDS_VISION_TEST_OBJECT
    assert env.OPENAI_COMMANDS_FUNCTION_BASH_TEST_OBJECT
    assert env.VISUALYZE_PORT
    assert env.OPENAI_GPT_DEFAULT_MODEL
    assert env.LITERATURE_REVIEW_OBJECT
    assert env.LITERATURE_REVIEW_TEST_FILENAME
    assert env.LITERATURE_REVIEW_TEST_QUESTIONS
