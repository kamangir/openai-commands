#! /usr/bin/env bash

function test_openai_commands_browse() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    abcli_eval ,$options \
        "openai_commands browse"
    [[ $? -ne 0 ]] && return 1

    abcli_eval ,$options \
        "openai_commands browse actions"
    [[ $? -ne 0 ]] && return 1

    abcli_eval ,$options \
        "openai_commands browse dashboard"
}
