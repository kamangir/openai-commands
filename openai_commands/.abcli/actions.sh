#! /usr/bin/env bash

function openai_commands_action_git_before_push() {
    [[ "$(abcli_git get_branch)" == "main" ]] &&
        openai_commands pypi build
}
