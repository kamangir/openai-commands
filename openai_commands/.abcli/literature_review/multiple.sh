#! /usr/bin/env bash

function literature_review_multiple() {
    local options=$1
    local workflow_options=$2
    local review_options=$3

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local args=$LITERATURE_REVIEW_ARGS
        options="${EOP}dryrun,${EOPE}publish,questions=<question1+question2>$EOP,suffix=<suffix>$EOPE"
        workflow_options="${EOP}dryrun,${EOPE}to=$NBS_RUNNERS_LIST"
        review_options="${EOP}dryrun,${EOPE}publish"
        abcli_show_usage "@litrev multiple$ABCUL[$options]$ABCUL[$workflow_options]$ABCUL[$review_options]$ABCUL[$LITERATURE_REVIEW_OBJECT|<object-name>]$ABCUL$args" \
            "ask multiple multiple-choice questions about the list of studies in <object-name>.${ABCUL2}input: <object-name>/<filename>.csv, column: Abstract.${ABCUL2}questions: <question1.yaml>, <question2.yaml>,... .${ABCUL2}output: <object-name>-<suffix>/<filename>-<suffix>.csv, columns: <question1>, <question2>, ... .${ABCUL2}<suffix> defaults to <question1-question2>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_publish=$(abcli_option_int "$options" publish 0)

    local list_of_questions=$(abcli_option "$options" questions)
    if [ -z "$list_of_questions" ]; then
        abcli_log_error "-literature review: question not found."
        return 1
    fi
    abcli_log_list "$list_of_questions" \
        --before "" \
        --delim + \
        --after "question(s)"

    local suffix=$(abcli_option "$options" suffix)
    local list_of_questions_safe=$(echo "$list_of_questions" | tr + -)
    if [ -z "$suffix" ]; then
        suffix=$list_of_questions_safe
    else
        suffix=$list_of_questions_safe-$suffix
    fi

    local runner_type=$(abcli_option "$options" to generic)

    local object_name=literature_review-$suffix-$(abcli_string_timestamp)

    # generate a workflow in $object_name
    abcli_log "🪄"

    workflow submit \
        ~download,dryrun=$do_dryrun,to=$runner_type \
        $object_name
}
