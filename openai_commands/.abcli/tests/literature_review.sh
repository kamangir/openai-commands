#! /usr/bin/env bash

function test_openai_commands_literature_review() {
    local options=$1

    literature_review choices=$LITERATURE_REVIEW_TEST_CHOICES,~upload,$options \
        $LITERATURE_REVIEW_OBJECT \
        --count 2 \
        --filename $LITERATURE_REVIEW_TEST_FILENAME
}
