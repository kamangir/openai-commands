#! /usr/bin/env bash

function test_openai_commands_complete() {
    openai_commands \
        complete \
        "Describe Mathematics in seven words."
}
