#! /usr/bin/env bash

function test_openai_commands_generate_text() {
    openai_commands \
        generate_text \
        "Describe Mathematics in seven words."
}
