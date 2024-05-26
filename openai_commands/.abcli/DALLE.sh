#! /usr/bin/env bash

# https://platform.openai.com/docs/api-reference/images/create-edit#images/create-edit-size
export DALL_E_BRUSH_SIZES="256|512|1024"

function DALL-E() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == help ]; then
        local options="brush=tiling|randomwalk,brush_size=$DALL_E_BRUSH_SIZES,~dryrun,lines=<5>,publish,url,verbose"
        abcli_show_usage "DALL-E render$ABCUL[$options]${ABCUL}input.txt|https://allpoetry.com/16-bit-Intel-8088-chip$ABCUL[output.png]<args>" \
            "render input.txt|url -> output.png."
        return
    fi

    if [ "$task" == render ]; then
        local options=$2

        python3 -m openai_commands.DALLE \
            render \
            --options "$options" \
            --source "$3" \
            --destination "$4" \
            "${@:5}"

        aiart_publish generator=DALL-E,$options

        return
    fi

    abcli_log_error "-DALLE: $task: command not found."
    return 1
}
