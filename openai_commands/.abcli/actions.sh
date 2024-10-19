#! /usr/bin/env bash

function openai_commands_action_git_before_push() {
    openai_commands build_README
    [[ $? -ne 0 ]] && return 1

    [[ "$(abcli_git get_branch)" != "main" ]] &&
        return 0

    openai_commands pypi build
}
