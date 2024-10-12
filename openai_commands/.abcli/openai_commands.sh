#! /usr/bin/env bash

function openai_commands() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ]; then
        literature_review "$@"

        openai_commands_browse "$@"
        openai_commands_complete "$@"
        openai_commands_generate "$@"
        openai_commands_gpt "$@"
        openai_commands_images "$@"
        openai_commands_transform "$@"
        openai_commands_vision "$@"
        openai_commands_VisuaLyze "$@"
        DALL-E "$@"
        return
    fi

    abcli_generic_task \
        plugin=openai_commands,task=$task \
        "${@:2}"
}

abcli_source_caller_suffix_path /tests

abcli_env_dot_load \
    caller,ssm,plugin=openai_commands,suffix=/../..

abcli_env_dot_load \
    caller,filename=config.env,suffix=/..

abcli_log $(openai_commands version --show_icon 1)
