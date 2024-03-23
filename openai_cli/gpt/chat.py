"""
This Python script enables real-time conversation with OpenAI's ChatGPT model through the terminal.
Generated by ChatGPT, this script establishes a session where the user can interactively ask questions
or have a dialogue with the ChatGPT model. The user's input is sent to the ChatGPT API, and the model's
responses are displayed in the terminal, facilitating a conversational interface. Ensure you have the `openai`
Python package installed and an OpenAI API key set before running this script.

committed in its original form and then modified by Arash Abadpour - arash.abadpour@gmail.com.
"""

import os
from typing import List, Any
import argparse
from openai import OpenAI
from abcli import file, path
from openai_cli import VERSION
from openai_cli.env import OPENAI_API_KEY
from openai_cli.gpt import NAME
from openai_cli.logger import logger

FULL_NAME = f"{NAME}-{VERSION}"

client = OpenAI(api_key=OPENAI_API_KEY)


def chat_with_openai(
    object_path: str = "",
    script_mode: bool = False,
    script: List[str] = [],
) -> bool:
    logger.info(FULL_NAME)

    conversation = []
    logger.info("ChatGPT: Hello! How can I assist you today?")

    index = -1
    while True:
        index += 1

        if script_mode:
            if index >= len(script):
                logger.info("end of script.")
                break

            logger.info(
                "script: line #{}/{}: {}".format(
                    index + 1,
                    len(script),
                    script[index],
                )
            )

        user_input = script[index] if script_mode else input("(?:help) > ")

        if user_input in ["?", "help"]:
            logger.info("exit: exit.")
            logger.info("version: show version.")
            continue
        if user_input == "version":
            logger.info(FULL_NAME)
            continue
        if user_input == "exit":
            break

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}],
            max_tokens=150,
        )

        answer = response.choices[0].message.content.strip()
        logger.info(f"ChatGPT: {answer}")

        conversation.append(
            {
                "user_input": user_input,
                "answer": answer,
            }
        )

    return not (object_path) or file.save_yaml(
        os.path.join(
            object_path,
            f"{path.name(object_path)}.yaml",
        ),
        {
            "conversation": conversation,
            "created-by": FULL_NAME,
            "script_mode": script_mode,
        },
    )


def list_models(log: bool = False) -> List[Any]:
    list_of_models = client.models.list().data

    if log:
        logger.info(f"{len(list_of_models)} model(s)")
        for index, model in enumerate(list_of_models):
            logger.info(f" #{index}: {model}")