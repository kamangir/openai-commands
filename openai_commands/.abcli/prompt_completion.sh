#! /usr/bin/env bash

function openai_commands_complete() {
    python3 -m openai_commands.completion \
        complete \
        --prompt "$1" \
        "${@:2}"
}
