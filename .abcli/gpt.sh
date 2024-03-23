#! /usr/bin/env bash

function openai_gpt() {
    local task=$(abcli_unpack_keyword "$1" help)

    if [ "$task" == help ]; then
        abcli_show_usage "gpt <args>" \
            "start gpt."

        if [ "$(abcli_keyword_is $2 verbose)" == true ]; then
            python3 -m openai_cli.gpt --help
        fi
        return
    fi

    python3 -m openai_cli.gpt "${@:2}"
}
