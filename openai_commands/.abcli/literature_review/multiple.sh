#! /usr/bin/env bash

function literature_review_multiple() {
    local options=$1
    local workflow_options=$2
    local review_options=$3

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local args=$LITERATURE_REVIEW_ARGS
        options="${EOP}dryrun,${EOPE}publish,questions=<question1+question2+...>$EOP,suffix=<suffix>$EOPE"
        workflow_options="${EOP}dryrun,${EOPE}to=$NBS_RUNNERS_LIST"
        review_options="${EOP}dryrun,${EOPE}publish"
        abcli_show_usage "@litrev multiple$ABCUL[$options]$ABCUL[$workflow_options]$ABCUL[$review_options]$ABCUL[$LITERATURE_REVIEW_OBJECT|<object-name>]$ABCUL$args" \
            "ask multiple multiple-choice questions about the list of studies in <object-name>.${ABCUL2}input: <object-name>/<filename>.csv, column: Abstract.${ABCUL2}questions: <object-name>/<question1>.yaml, <question2>.yaml, ... .${ABCUL2}output: <object-name>-<suffix>-<question1>-<question-2>-<...>/<filename>.csv, columns: <question1>, <question2>, ... ."
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

    local suffix=$(abcli_option "$options" suffix $(abcli_string_timestamp_short))

    local job_name=literature_review-$(abcli_string_timestamp)

    local object_name=$(abcli_clarify_object $4 $LITERATURE_REVIEW_OBJECT)

    local args=$(echo "${@:5}" | $abcli_base64)

    local do_dryrun_review=$(abcli_option_int "$review_options" dryrun 0)

    abcli_log "multiple literature review, job: $job_name -$list_of_questions-> suffix: $suffix ..."

    abcli_eval dryrun=$do_dryrun \
        python3 -m openai_commands.literature_review \
        generate_multiple_review_workflow \
        --do_dryrun $do_dryrun_review \
        --job_name $job_name \
        --list_of_questions $list_of_questions \
        --object_name $object_name \
        --review_options "$review_options" \
        --do_publish $do_publish \
        --suffix $suffix \
        --args $args
    [[ $? -ne 0 ]] && return 1

    workflow submit \
        ~download,$workflow_options \
        $job_name
}
