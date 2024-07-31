#! /usr/bin/env bash

function openai_commands() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ]; then
        literature_review "$@"

        openai_commands_complete "$@"

        abcli_show_usage "@openai dashboard" \
            "browse OpenAI dashboard."

        openai_commands_generate "$@"
        openai_commands_gpt "$@"
        openai_commands_images "$@"
        openai_commands_transform "$@"
        openai_commands_vision "$@"
        openai_commands_VisuaLyze "$@"
        DALL-E "$@"
        return
    fi

    if [ "$task" == "dashboard" ]; then
        abcli_browse https://beta.openai.com/account/usage
        return
    fi

    abcli_generic_task \
        plugin=openai_commands,task=$task \
        "${@:2}"
}

abcli_source_path - caller,suffix=/tests

abcli_log $(openai_commands version --show_icon 1)

abcli_env dot load \
    plugin=openai_commands
abcli_env dot load \
    filename=openai_commands/config.env,plugin=openai_commands
