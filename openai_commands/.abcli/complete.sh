#! /usr/bin/env bash

function openai_commands_completion() {
    openai_commands_complete "$@"
}

function openai_commands_complete() {
    local task=$(abcli_unpack_keyword "$1" help)

    if [ "$task" == help ]; then
        abcli_show_usage "@openai complete \"<prompt>\"$ABCUL[-]$ABCUL[--max_tokens <2000>]$ABCUL[--verbose 1]" \
            "complete <prompt>."

        abcli_show_usage "@openai completion describe <plugin-name>" \
            "describe <plugin-name> for @openai"
        return
    fi

    if [ "$task" == "describe" ]; then
        local plugin_name=$(abcli_clarify_input $2 abcli)

        export abcli_show_usage_destination=$abcli_object_path/$plugin_name-description.yaml

        abcli_log "$plugin_name -> $abcli_show_usage_destination"

        $plugin_name help

        python3 -m openai_commands.completion \
            pre_process_bash_description \
            --filename "$abcli_show_usage_destination" \
            "${@:3}"

        unset abcli_show_usage_destination

        abcli_cat $abcli_object_path/$plugin_name-description.txt

        return
    fi

    local options=$2

    python3 -m openai_commands.completion \
        complete \
        --prompt "$1" \
        "${@:3}"
}
