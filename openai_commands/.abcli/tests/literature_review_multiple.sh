#! /usr/bin/env bash

function test_openai_commands_literature_review_multiple() {
    local options=$1

    literature_review multiple \
        questions=study-type+screening-result,$options \
        to=local \
        - \
        $LITERATURE_REVIEW_OBJECT \
        --count 2 \
        --filename review_463333_screen_csv_20240730130035
}
