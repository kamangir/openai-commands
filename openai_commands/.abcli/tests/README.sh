#! /usr/bin/env bash

function openai_commands_geo_README() {
    local options=$1

    abcli_eval ,$options \
        openai_commands build_README
}
