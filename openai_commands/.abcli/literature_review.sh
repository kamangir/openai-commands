#! /usr/bin/env bash

export LITERATURE_REVIEW_ARGS="[--count <-1>]$ABCUL[--filename <filename>]$ABCUL[--overwrite 1]$ABCUL[--verbose 1]"

function literature_review() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local args=$LITERATURE_REVIEW_ARGS
        options="${EOP}dryrun,~download,${EOPE}publish,question=<question>$EOP,suffix=<suffix>,~upload$EOPE"
        abcli_show_usage "@litrev$ABCUL[$options]$ABCUL[$LITERATURE_REVIEW_OBJECT|<object-name>]$ABCUL$args" \
            "ask a multiple-choice question about the list of studies in <object-name>.${ABCUL2}input: <object-name>/<filename>.csv, column: Abstract.${ABCUL2}question: <question.yaml>.${ABCUL2}output: <object-name>-<suffix>/<filename>-<suffix>.csv, column: <suffix>.${ABCUL2}<suffix> defaults to <question>."

        literature_review_multiple "$@"
        return
    fi

    if [ $(abcli_option_int "$options" multiple 0) == 1 ]; then
        literature_review_multiple "${@:2}"
        return
    fi

    local question=$(abcli_option "$options" question)
    if [ -z "$question" ]; then
        abcli_error "-literature review: question not found."
        return 1
    fi

    local suffix=$(abcli_option "$options" suffix)
    if [ -z "$suffix" ]; then
        suffix=$question
    else
        suffix=$question-$suffix
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_publish=$(abcli_option_int "$options" publish 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))

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

abcli_source_path - caller,suffix=/literature_review
