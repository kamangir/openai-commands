#! /usr/bin/env bash

function test_openai_commands_help() {
    local options=$1

    local module
    for module in \
        "@litrev" \
        "@litrev combine" \
        "@litrev multiple" \
        \
        "@openai browse" \
        \
        "@openai complete" \
        \
        "@openai generate_image" \
        \
        "@openai"; do
        abcli_eval ,$options \
            abcli_help $module
        [[ $? -ne 0 ]] && return 1
    done

    return 0
}
