#! /usr/bin/env bash

function openai_commands_complete() {
    python3 -m openai_commands.prompt_completion \
        complete \
        --prompt "$1" \
        "${@:2}"
}
