from openai_commands import README


def test_build_README():
    assert README.build()
