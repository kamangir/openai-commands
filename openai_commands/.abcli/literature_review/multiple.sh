#! /usr/bin/env bash

function openai_commands_literature_review_multiple() {
    local options=$1
    local workflow_options=$2
    local review_options=$3

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_publish=$(abcli_option_int "$options" publish 0)

    local list_of_questions=$(abcli_option "$options" questions)
    if [ -z "$list_of_questions" ]; then
        abcli_log_error "@litrev: question not found."
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

    blueflow_workflow_submit \
        ~download,$workflow_options \
        $job_name
}
