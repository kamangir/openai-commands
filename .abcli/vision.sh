#! /usr/bin/env bash

function openai_vision() {
    local prompt=$1

    if [ "$prompt" == "help" ]; then
        local options="auto|low|high,dryrun,prefix=<prefix>,~upload"
        local args="[--count <2>]$ABCUL[--extension <jpg>]$ABCUL[--verbose 1]"
        abcli_show_usage "openai vision \"prompt\"$ABCUL[$options]$ABCUL<.|object-name>$ABCUL$args" \
            "complete <prompt> given the image(s) in <object-name>."
        return
    fi

    local options=$2
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload 1)

    local object_name=$(abcli_clarify_object "$3" .)

    [[ "$do_upload" == 1 ]] &&
        abcli_upload object $object_name

    abcli_eval dryrun=$do_dryrun \
        python3 -m openai_cli.vision \
        complete \
        --prompt "$prompt" \
        --detail $(abcli_option_choice "$options" auto,low,high auto) \
        --object_name $object_name \
        --prefix $(abcli_option "$options" prefix none) \
        "${@:4}"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload object $object_name
}
