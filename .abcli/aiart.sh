#! /usr/bin/env bash

function openai_generate() {
    aiart_generate \
        "$1" \
        app=openai,$2 \
        "${@:3}"
}

function openai_transform() {
    aiart_transform \
        app=openai,$1 \
        "${@:2}"
}
