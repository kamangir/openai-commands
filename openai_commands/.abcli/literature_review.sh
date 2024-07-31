#! /usr/bin/env bash

function literature_review() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="dryrun,~download,~upload"
        local args="[--count <-1>]$ABCUL[--filename <filename.csv>]$ABCUL[--questions <questions.yaml>]"
        abcli_show_usage "literature_review$ABCUL[$options]$ABCUL[.|<object-name>]$ABCUL[<args>]" \
            "run literature review on <object-name>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))
    local do_upload=$(abcli_option_int "$options" uploa $(abcli_not $do_dryrun))

    local object_name=$(abcli_clarify_object $2 .)

    [[ "$do_download" == 1 ]] &&
        abcli_download - $object_name

    abcli_log "literature_review: $object_name ..."

    abcli_eval dryrun dryrun=$do_dryrun \
        python3 -m openai_commands.literature_review \
        --object_name $object_name \
        "${@:3}"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return 0
}
