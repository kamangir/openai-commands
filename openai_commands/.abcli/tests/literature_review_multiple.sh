#! /usr/bin/env bash

function test_openai_commands_literature_review_multiple() {
    local options=$1
    local list_of_runners=$(abcli_option "$options" runner "local|aws_batch")

    local runner
    local suffix
    for runner in $(echo $list_of_runners | tr \| " "); do
        suffix=test-litrev-multiple-$runner

        abcli_log "📜 testing runner=$runner -> $suffix ..."

        literature_review multiple \
            questions=study-type+screening-result,suffix=$suffix,$options \
            to=$runner,$2 \
            - \
            $LITERATURE_REVIEW_OBJECT \
            --count 2 \
            --filename review_463333_screen_csv_20240730130035 \
            "${@:3}"

        abcli_hr
    done
}
