#! /usr/bin/env bash

function literature_review() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="choices=<choices>$EOP,dryrun,~download,publish,suffix=<suffix>,~upload$EOPE"
        local args="[--count <-1>]$ABCUL[--filename <filename>]$ABCUL[--overwrite 1]$ABCUL[--verbose 1]"
        abcli_show_usage "@litrev$ABCUL[$options]$ABCUL[$LITERATURE_REVIEW_OBJECT|<object-name>]$ABCUL$args" \
            "<object-name>/<filename>.csv -literature-review-@-<choices.yaml>-> <object-name>-<suffix>/<filename>-<choices>.csv."
        return
    fi

    local choices=$(abcli_option "$options" choices choices1)
    local suffix=$(abcli_option "$options" suffix $choices)
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

    abcli_log "literature review: $input_object_name -$choices-> $output_object_name ..."

    abcli_eval dryrun=$do_dryrun \
        python3 -m openai_commands.literature_review \
        --choices $choices.yaml \
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
