#! /usr/bin/env bash

function openai_generate() {
    blue_stability_generate \
        "$1" \
        $(abcli_option_default "$2" app openai) \
        ${@:3}
}