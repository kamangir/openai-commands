#! /usr/bin/env bash

function DALL-E() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == help ] ; then
        abcli_show_usage "DALL-E render <filename>$ABCUL[brush=tiling|randomwalk,lines=<5>]" \
            "render <filename>."
        return
    fi

    if [ "$task" == render ] ; then
        local filename=$2

        local options=$3
        local brush=$(abcli_option "$options" brush tiling)
        local lines=$(abcli_option "$options" lines -1)

        python3 -m openai_cli.DALLE \
            render \
            --filename $filename \
            --brush $brush \
            --lines $lines \
            "${@:4}"

        return
    fi

    abcli_log_error "-DALLE: $task: command not found."
}