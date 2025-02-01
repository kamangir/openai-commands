#! /usr/bin/env bash

function openai_commands_browse() {
    local options=$1
    local do_actions=$(abcli_option_int "$options" actions 0)
    local do_dashboard=$(abcli_option_int "$options" dashboard 0)

    local url
    if [[ "$do_dashboard" == 1 ]]; then
        url="https://beta.openai.com/account/usage"
    else
        url="https://github.com/kamangir/openai-commands"

        [[ "$do_actions" == 1 ]] &&
            url="$url/actions"
    fi

    abcli_browse $url
}
