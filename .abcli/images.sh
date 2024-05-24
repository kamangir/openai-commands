#! /usr/bin/env bash

export openai_commands_images_options="dryrun,filename=<filename.png>,~upload"

function openai_commands_images() {
    local task=$1

    if [ "$task" == "help" ]; then
        local args="[--verbose 1]"
        abcli_show_usage "@openai images generate$ABCUL[$openai_commands_images_options]$ABCUL\"<prompt+prompt+prompt>\"$ABCUL[.|<object-name>]$ABCUL$args" \
            "generate an image for <prompt> in <object-name>."
        return
    fi

    local options=$2
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload 1)
    local filename=$(abcli_option "$options" filename $(abcli_string_timestamp).png)

    local prompt=$3

    local object_name=$(abcli_clarify_object "$4" .)

    abcli_eval dryrun=$do_dryrun \
        python3 -m openai_commands.images \
        $task \
        --filename $filename \
        --options "$options" \
        --prompt "\"$prompt\"" \
        --object_name $object_name \
        "${@:5}"

    if [[ "$do_upload" == 1 ]]; then
        abcli_upload - $object_name
    fi
}
