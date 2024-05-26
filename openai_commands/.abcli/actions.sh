#! /usr/bin/env bash

function openai_commands_action_git_before_push() {
    openai_commands pypi build
}
