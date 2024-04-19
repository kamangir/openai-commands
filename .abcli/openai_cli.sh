#! /usr/bin/env bash

function openai_cli() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ]; then
        openai_cli_complete "$@"
        openai_cli_conda "$@"

        abcli_show_usage "@openai dashboard" \
            "browse OpenAI dashboard."

        openai_cli_generate "$@"
        openai_cli_gpt "$@"
        openai_cli_images "$@"

        local task
        for task in pylint pytest test; do
            openai_cli $task "$@"
        done

        openai_cli_transform "$@"
        openai_cli_vision "$@"
        openai_cli_VisuaLyze "$@"
        DALL-E "$@"
        return
    fi

    local function_name=openai_cli_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    if [ "$task" == "dashboard" ]; then
        abcli_browse_url https://beta.openai.com/account/usage
        return
    fi

    if [ "$task" == "init" ]; then
        abcli_init openai_cli "${@:2}"
        conda activate openai_cli
        return
    fi

    if [[ "|pylint|pytest|test|" == *"|$task|"* ]]; then
        abcli_${task} plugin=openai_cli,$2 \
            "${@:3}"
        return
    fi

    if [ "$task" == "version" ]; then
        python3 -m openai_cli version "${@:2}"
        return
    fi

    abcli_log_error "-openai_cli: $task: command not found."
    return 1
}

abcli_source_path \
    $abcli_path_git/openai-cli/.abcli/tests

abcli_env dot load \
    plugin=openai_cli
abcli_env dot load \
    filename=openai_cli/config.env,plugin=openai_cli
