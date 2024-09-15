#! /usr/bin/env bash

function openai_commands_gpt() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="dryrun,~upload"
        local args="[--model_name gpt-4-turbo-preview]"
        abcli_show_usage "gpt [$options]$ABCUL[-|<object-name>]$ABCUL$args" \
            "chat with gpt."

        openai_commands_gpt list_models "$@"

        if [ "$(abcli_keyword_is $2 verbose)" == true ]; then
            python3 -m openai_commands.gpt --help
        fi
        return
    fi

    if [ $(abcli_option_int "$options" list_models 0) == 1 ]; then
        local options=$2
        if [ $(abcli_option_int "$options" help 0) == 1 ]; then
            abcli_show_usage "gpt list_models [-]$ABCUL[--log 0]" \
                "list gpt models."
            return
        fi

        python3 -m openai_commands.gpt list_models \
            "${@:3}"
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))

    local object_name=$(abcli_clarify_object $2 gpt-chat-$(abcli_string_timestamp))
    local object_path=$ABCLI_OBJECT_ROOT/$object_name
    mkdir -p $object_path

    abcli_tags set $object_name gpt_chat

    abcli_eval dryrun=$do_dryrun \
        python3 -m openai_commands.gpt \
        chat_with_openai \
        --object_path $object_path \
        "${@:3}"

    if [[ "$do_upload" == 1 ]]; then
        abcli_upload - $object_name
    fi
}
