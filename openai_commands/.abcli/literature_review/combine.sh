#! /usr/bin/env bash

function openai_commands_literature_review_combine() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))
    local do_publish=$(abcli_option_int "$options" publish 0)

    local object_name_1=$(abcli_clarify_object $2 ...)
    local object_name_2=$(abcli_clarify_object $3 ..)
    if [[ "$do_download" == 1 ]]; then
        abcli_download - $object_name_1
        abcli_download - $object_name_2
    fi

    local object_name=$(abcli_clarify_object $4 .)

    abcli_log "combining $object_name_1 + $object_name_2 -> $object_name"

    abcli_eval dryrun=$do_dryrun \
        python3 -m openai_commands.literature_review \
        combine \
        --object_name $object_name \
        --object_name_1 $object_name_1 \
        --object_name_2 $object_name_2 \
        "${@:5}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    [[ "$do_publish" == 1 ]] &&
        abcli_publish tar $object_name

    return $status
}
