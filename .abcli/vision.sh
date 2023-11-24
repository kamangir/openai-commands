#! /usr/bin/env bash

function openai_vision() {
    local prompt=$1

    if [ "$prompt" == "help" ]; then
        local options="auto|low|high,~download,dryrun,prefix=<prefix>,~upload"
        local args="[--verbose 1]$ABCUL[--count <2>]$ABCUL[--extension <jpg>]"
        abcli_show_usage "openai vision \"prompt\"$ABCUL[$options]$ABCUL<.|object-name>$ABCUL$args" \
            "complete <prompt> given image(s)."
        return
    fi

    local options=$2
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download 1)
    local do_upload=$(abcli_option_int "$options" upload 1)

    local object_name=$(abcli_clarify_object "$3" .)

    [[ "$do_download" == 1 ]] &&
        abcli_download object $object_name

    abcli_eval dryrun=$do_dryrun \
        python3 -m openai_cli.vision \
        --detail $(abcli_option_choice "$options" auto,low,high auto) \
        --prefix $(abcli_option "$options" prefix none) \
        "${@:4}"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload object $object_name
}
