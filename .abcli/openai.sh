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
        local options=$2

        if [[ $(abcli_option_int "$options" help 0) == 0 ]] &&
            [[ "$task" != "pylint" ]]; then
            abcli_download - openai-completion-function-2d-v3
            abcli_download - 2023-11-12-12-03-40-85851
        fi

        abcli_${task} plugin=openai,$options \
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
