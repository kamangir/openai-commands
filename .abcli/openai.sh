#! /usr/bin/env bash

function openai() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_show_usage "openai dashboard" \
            "browse openai dashboard."
        openai_generate $@
        openai_transform $@
        return
    fi

    local function_name=openai_$task
    if [[ $(type -t $function_name) == "function" ]] ; then
        $function_name "${@:2}"
        return
    fi

    if [ "$task" == "dashboard" ] ; then
        abcli_browse_url https://beta.openai.com/account/usage
        return
    fi

    if [ "$task" == "version" ] ; then
        python3 -m openai_cli version
        return
    fi

    abcli_log_error "-openai: $task: command not found."
}