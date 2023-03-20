#! /usr/bin/env bash

function DALL-E() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == help ] ; then
        local options="brush=tiling|randomwalk,~dryrun,lines=<5>,url,verbose"
        abcli_show_usage "DALL-E render$ABCUL[$options]${ABCUL}input.txt|https://allpoetry.com/16-bit-Intel-8088-chip$ABCUL[output.png]" \
            "render input.txt -> output.png."
        return
    fi

    if [ "$task" == render ] ; then
        python3 -m openai_cli.DALLE \
            render \
            --options "$2" \
            --source "$3" \
            --destination "$4" \
            "${@:5}"
        return
    fi

    abcli_log_error "-DALLE: $task: command not found."
}