#! /usr/bin/env bash

function literature_review() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="dryrun,~download,~upload"
        local args="[--choices <choices.yaml>]$ABCUL[--count <-1>]$ABCUL[--filename <filename.csv>]$ABCUL[--overwrite 1]$ABCUL[--suffix <suffix>]$ABCUL[--verbose 1]"
        abcli_show_usage "@litrev$ABCUL[$options]$ABCUL[$LITERATURE_REVIEW_OBJECT|<object-name>]$ABCUL$args" \
            "<object-name>/<filename.csv> -literature-review-@-choices-> <filename-suffix.csv>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))

    local object_name=$(abcli_clarify_object $2 $LITERATURE_REVIEW_OBJECT)

    [[ "$do_download" == 1 ]] &&
        abcli_download - $object_name

    abcli_log "literature review: $object_name ..."

    abcli_eval dryrun=$do_dryrun \
        python3 -m openai_commands.literature_review \
        --object_name $object_name \
        "${@:3}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return $status
}
