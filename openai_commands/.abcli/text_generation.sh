#! /usr/bin/env bash

function openai_commands_generate_text() {
    python3 -m openai_commands.text_generation \
        generate_text \
        --prompt "$1" \
        "${@:2}"
}
