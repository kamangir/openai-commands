#! /usr/bin/env bash

function DALL-E() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == help ] ; then
        local options="brush=tiling|randomwalk,~dryrun,lines=<5>,publish,url,verbose"
        abcli_show_usage "DALL-E render$ABCUL[$options]${ABCUL}input.txt|https://allpoetry.com/16-bit-Intel-8088-chip$ABCUL[output.png]" \
            "render input.txt|url -> output.png."
        return
    fi

    if [ "$task" == render ] ; then
        local options=$2

        python3 -m openai_cli.DALLE \
            render \
            --options "$options" \
            --source "$3" \
            --destination "$4" \
            "${@:5}"

        aiart_create_html \
            $(abcli_option_default "$options" generator DALL-E)

        return
    fi

    abcli_log_error "-DALLE: $task: command not found."
}