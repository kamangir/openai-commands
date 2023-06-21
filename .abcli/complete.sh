#! /usr/bin/env bash

function openai_complete() {
    local task=$(abcli_unpack_keyword "$1" help)

    if [ "$task" == help ] ; then
        abcli_show_usage "openai complete \"prompt\"$ABCUL[-]$ABCUL[--max_tokens <2000>]$ABCUL[--verbose 1]" \
            "complete prompt."
        return
    fi

    local options=$2

    python3 -m openai_cli \
        complete \
        --prompt "$1" \
        "${@:3}"
}