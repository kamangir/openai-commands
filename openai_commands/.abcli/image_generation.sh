#! /usr/bin/env bash

function openai_commands_generate_image() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload 1)
    local filename=$(abcli_option "$options" filename $(abcli_string_timestamp).png)

    local prompt=$2

    local object_name=$(abcli_clarify_object "$3" openai-image-$(abcli_string_timestamp_short))

    abcli_eval dryrun=$do_dryrun \
        python3 -m openai_commands.image_generation \
        generate_image \
        --filename $filename \
        --prompt "\"$prompt\"" \
        --object_name $object_name \
        "${@:4}"
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return 0
}
