#! /usr/bin/env bash

export openai_commands_vision_options=""

function openai_commands_vision() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload 1)
    local detail=$(abcli_option_choice "$options" detail auto)

    local image_options=$2

    local prompt=$3

    local object_name=$(abcli_clarify_object "$4" .)
    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    abcli_eval dryrun=$do_dryrun \
        python3 -m openai_commands.vision \
        complete \
        --detail $detail \
        --object_name $object_name \
        --image_options ,$image_options \
        --prompt "\"$prompt\"" \
        "${@:5}"
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name
}
