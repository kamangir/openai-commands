#! /usr/bin/env bash

function DALLE() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == help ] ; then
        abcli_show_usage "DALLE render <filename>$ABCUL[brush=tiling|randomwalk]" \
            "render <filename>."
        return
    fi

    if [ "$task" == render ] ; then
        local filename=$2

        local options=$3
        local brush=$(abcli_option "$options" brush tiling)

        python3 -m openai_cli.DALLE \
            render \
            --filename $filename \
            --brush $brush

        return
    fi

    abcli_log_error "-DALLE: $task: command not found."
}