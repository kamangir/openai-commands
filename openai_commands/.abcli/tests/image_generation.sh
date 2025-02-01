#! /usr/bin/env bash

function test_openai_commands_complete() {
    local options=$1

    openai_commands_generate_image \
        ~upload,$options \
        "a person flying through the streets of Vancouver." \
        test_openai_commands_complete-$(abcli_string_timestamp_short) \
        --verbose 1
}
