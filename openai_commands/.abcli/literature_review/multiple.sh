#! /usr/bin/env bash

function literature_review_multiple() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local args=$LITERATURE_REVIEW_ARGS
        options="multiple,question=<question1+question2>,to=$NBS_RUNNERS_LIST$LITERATURE_REVIEW_BASE_OPTIONS"
        abcli_show_usage "@litrev$ABCUL[$options]$ABCUL[$LITERATURE_REVIEW_OBJECT|<object-name>]$ABCUL$args" \
            "ask multiple multiple-choice questions about a list of studies.${ABCUL2}input: <object-name>/<filename>.csv, column: Abstract.${ABCUL2}questions: <question1.yaml>, <question2.yaml>,... .${ABCUL2}output: <object-name>-<suffix>/<filename>-<suffix>.csv, columns: <question1>, <question2>, ... .${ABCUL2}<suffix> defaults to <question1-question2>."
        return
    fi

    local question=$(abcli_option "$options" question)
    if [ -z "$question" ]; then
        abcli_log_error "-literature review: question not found."
        return 1
    fi
    abcli_log_list "$question" \
        --before "" \
        --delim + \
        --after "question(s)"

    local runner_type=$(abcli_option "$options" to generic)

    local object_name=literature_review-$suffix-$(abcli_string_timestamp)

    # generate a workflow in $object_name
    abcli_log "🪄"

    workflow submit \
        ~download,dryrun=$do_dryrun,to=$runner_type \
        $object_name
}
