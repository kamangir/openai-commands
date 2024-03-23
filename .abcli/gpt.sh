#! /usr/bin/env bash

function openai_gpt() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="dryrun,~upload"
        abcli_show_usage "gpt [$options]$ABCUL[-|<object-name>]$ABCUL<args>" \
            "chat with gpt."

        if [ "$(abcli_keyword_is $2 verbose)" == true ]; then
            python3 -m openai_cli.gpt --help
        fi
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))

    local object_name=$(abcli_clarify_object $2 gpt-chat-$(abcli_string_timestamp))
    local object_path=$abcli_object_root/$object_name
    mkdir -p $object_path

    abcli_tag set $object_name gpt_chat

    abcli_eval dryrun=$do_dryrun \
        python3 -m openai_cli.gpt \
        --object_path $object_path \
        "${@:3}"

    if [[ "$do_upload" == 1 ]]; then
        abcli_upload - $object_name
    fi
}
