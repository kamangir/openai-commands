#! /usr/bin/env bash

function openai_generate() {
    aiart_generate \
        "$1" \
        $(abcli_option_default "$2" app openai) \
        "${@:3}"
}

function openai_transform() {
    aiart_transform \
        $(abcli_option_default "$1" app openai) \
        ${@:2}
}