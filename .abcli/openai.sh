#! /usr/bin/env bash

function openai() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        openai_generate $@

        abcli_show_usage "openai version" \
            "show openai version."

        if [ "$(abcli_keyword_is $2 verbose)" == true ] ; then
            python3 -m openai_cli --help
        fi

        return
    fi

    local function_name=openai_$task
    if [[ $(type -t $function_name) == "function" ]] ; then
        $function_name ${@:2}
        return
    fi

    if [ "$task" == "version" ] ; then
        abcli_log $(python3 -m openai_cli version)
        return
    fi

    abcli_log_error "-openai: $task: command not found."
}