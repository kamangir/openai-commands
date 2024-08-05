#! /usr/bin/env bash

function literature_review() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local base_options="$EOP,dryrun,~download,publish,suffix=<suffix>,~upload$EOPE"
        local args="[--count <-1>]$ABCUL[--filename <filename>]$ABCUL[--overwrite 1]$ABCUL[--verbose 1]"

        options="question=<question>$base_options"
        abcli_show_usage "@litrev$ABCUL[$options]$ABCUL[$LITERATURE_REVIEW_OBJECT|<object-name>]$ABCUL$args" \
            "ask a multiple-choice question about a list of studies.${ABCUL2}input: <object-name>/<filename>.csv, column: Abstract.${ABCUL2}question: <question.yaml>.${ABCUL2}output: <object-name>-<suffix>/<filename>-<suffix>.csv, column: <suffix>.${ABCUL2}<suffix> defaults to <question>."

        options="multiple,question=<question1+question2>,to=$NBS_RUNNERS_LIST$base_options"
        abcli_show_usage "@litrev$ABCUL[$options]$ABCUL[$LITERATURE_REVIEW_OBJECT|<object-name>]$ABCUL$args" \
            "ask multiple multiple-choice questions about a list of studies.${ABCUL2}input: <object-name>/<filename>.csv, column: Abstract.${ABCUL2}questions: <question1.yaml>, <question2.yaml>,... .${ABCUL2}output: <object-name>-<suffix>/<filename>-<suffix>.csv, columns: <question1>, <question2>, ... .${ABCUL2}<suffix> defaults to <question1-question2>."
        return
    fi

    local question=$(abcli_option "$options" question question1)
    local suffix=$(echo $question | tr + -)
    suffix=$(abcli_option "$options" suffix $suffix)
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_publish=$(abcli_option_int "$options" publish 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))
    local multiple_questions=$(abcli_option_has "$options" multiple 0)

    if [[ "$multiple_questions" == 1 ]]; then
        abcli_log_list "$multiple_questions" \
            --before "" \
            --delim + \
            --after "question(s)"

        abcli_log "🪄"
        return
    fi

    local input_object_name=$(abcli_clarify_object $2 $LITERATURE_REVIEW_OBJECT)
    local output_object_name=$input_object_name-$suffix
    if [[ "$do_download" == 1 ]]; then
        abcli_download - $input_object_name
        abcli_download - $output_object_name
    fi

    abcli_log "literature review: $input_object_name -$question-> $output_object_name ..."

    abcli_eval dryrun=$do_dryrun \
        python3 -m openai_commands.literature_review \
        --question_filename $question.yaml \
        --input_object_name $input_object_name \
        --output_object_name $output_object_name \
        --suffix $suffix \
        "${@:3}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $output_object_name

    [[ "$do_publish" == 1 ]] &&
        abcli_publish tar $output_object_name

    return $status
}
