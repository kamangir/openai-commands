from setuptools import setup

from openai import NAME, VERSION

setup(
    name=NAME,
    author="arash@kamangir.net",
    version=VERSION,
    description="Bash access to the OpenAI API",
    packages=[NAME],
)
