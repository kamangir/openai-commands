#! /usr/bin/env bash

function openai() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ]; then
        openai_complete "$@"
        openai_conda "$@"

        abcli_show_usage "openai dashboard" \
            "browse openai dashboard."

        openai_generate "$@"
        openai_images "$@"

        local task
        for task in pylint pytest test; do
            openai $task "$@"
        done

        openai_transform "$@"
        openai_vision "$@"
        DALL-E "$@"
        return
    fi

    local function_name=openai_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    if [ "$task" == "dashboard" ]; then
        abcli_browse_url https://beta.openai.com/account/usage
        return
    fi

    if [ "$task" == "init" ]; then
        abcli_init openai "${@:2}"
        conda activate openai
        return
    fi

    if [[ "|pylint|pytest|test|" == *"|$task|"* ]]; then
        abcli_${task} plugin=openai,$2 \
            "${@:3}"
        return
    fi

    if [ "$task" == "version" ]; then
        python3 -m openai_cli version "${@:2}"
        return
    fi

    abcli_log_error "-openai: $task: command not found."
}

abcli_source_path \
    $abcli_path_git/openai/.abcli/tests

abcli_env dot load \
    plugin=openai
abcli_env dot load \
    filename=config.env,plugin=openai
