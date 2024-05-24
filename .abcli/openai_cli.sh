#! /usr/bin/env bash

function openai_commands() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ]; then
        openai_cli_complete "$@"

        abcli_show_usage "@openai dashboard" \
            "browse OpenAI dashboard."

        openai_cli_generate "$@"
        openai_cli_gpt "$@"
        openai_cli_images "$@"
        openai_cli_transform "$@"
        openai_cli_vision "$@"
        openai_cli_VisuaLyze "$@"
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

abcli_source_path \
    $abcli_path_git/openai-commands/.abcli/tests

abcli_env dot load \
    plugin=openai_commands
abcli_env dot load \
    filename=openai_commands/config.env,plugin=openai_commands
