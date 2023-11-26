#! /usr/bin/env bash

function openai() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ]; then
        openai version \\n

        openai_complete "$@"
        openai_conda "$@"

        abcli_show_usage "openai dashboard" \
            "browse openai dashboard."

        openai_generate "$@"

        abcli_show_usage "openai pytest" \
            "test openai."

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

    if [ "$task" == "pytest" ]; then
        abcli_download object openai-completion-function-2d-v3
        abcli_download object 2023-11-12-12-03-40-85851

        abcli_pytest plugin=openai,$2 \
            "${@:3}"
        return
    fi

    if [ "$task" == "version" ]; then
        abcli_log "🛠️ $(python3 -m openai_cli version --show_description 1)${@:2}"
        return
    fi

    abcli_log_error "-openai: $task: command not found."
}
