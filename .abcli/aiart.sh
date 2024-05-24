#! /usr/bin/env bash

function openai_cli_generate() {
    aiart_generate \
        "$1" \
        app=openai_commands,$2 \
        "${@:3}"
}

function openai_cli_transform() {
    aiart_transform \
        app=openai_commands,$1 \
        "${@:2}"
}
