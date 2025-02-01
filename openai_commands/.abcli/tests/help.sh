#! /usr/bin/env bash

function test_openai_commands_help() {
    local options=$1

    # TODO: add, (historic)
    # - "openai_commands completion describe" \
    # - "openai_commands images generate"
    # - "DALL-E render" \

    # TODO: add,
    #    "literature_review" \
    #    "literature_review combine" \
    #    "literature_review multiple" \
    #    "openai_commands completion" \
    #    "openai_commands generate" \
    #    "openai_commands generate image" \
    #    "openai_commands generate video" \
    #    "openai_commands generate validate" \
    #    "openai_commands images" \
    #    "openai_commands transform" \
    #    "openai_commands vision" \
    #    \
    #    "openai_commands_gpt" \
    #    "openai_commands_gpt list_models" \
    #    \
    #    "VisuaLyze" \
    #    "VisuaLyze browse" \
    #    "VisuaLyze run" \
    #     "DALL-E"

    local module
    for module in \
        "@openai browse" \
        "@openai complete" \
        \
        "@openai"; do
        abcli_eval ,$options \
            abcli_help $module
        [[ $? -ne 0 ]] && return 1
    done

    return 0
}
