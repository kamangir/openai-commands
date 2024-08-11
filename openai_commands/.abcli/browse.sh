#! /usr/bin/env bash

function openai_commands_browse() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="dashboard"
        abcli_show_usage "@openai browse$ABCUL[$options]" \
            "browse OpenAI."
        return
    fi

    local url="https://beta.openai.com/account/usage"

    abcli_browse $url
}
