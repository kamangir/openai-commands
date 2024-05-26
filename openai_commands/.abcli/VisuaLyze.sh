#! /usr/bin/env bash

function VisuaLyze() {
    openai_commands_VisuaLyze "$@"
}

function openai_commands_VisuaLyze() {
    local task=$(abcli_unpack_keyword $1 run)

    if [[ "$task" == help ]]; then
        openai_commands_VisuaLyze browse "$@"
        openai_commands_VisuaLyze run "$@"
        return
    fi

    local options=$2
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    if [[ "$task" == browse ]]; then
        if [ $(abcli_option_int "$options" help 0) == 1 ]; then
            abcli_show_usage "VisuaLyze browse" \
                "browse VisuaLyze."
            return
        fi

        abcli_browse http://127.0.0.1:$VISUALYZE_PORT/
        return
    fi

    if [[ "$task" == run ]]; then
        if [ $(abcli_option_int "$options" help 0) == 1 ]; then
            local options="~browse,dryrun"
            abcli_show_usage "VisuaLyze run$ABCUL[$options]$ABCUL[-|<object-name>]" \
                "run VisuaLyze."
            return
        fi

        local do_browse=$(abcli_option "$options" browse 1)

        [[ "$do_browse" == 1 ]] &&
            abcli_browse http://127.0.0.1:$VISUALYZE_PORT/

        # https://stackoverflow.com/a/72797062/17619982
        abcli_eval \
            path=$abcli_path_git/openai-commands/openai_commands/VisuaLyze/flask/,$options \
            flask \
            --app VisuaLyze \
            run \
            --port $VISUALYZE_PORT
        return
    fi

    abcli_log_error "-@openai: VisuaLyze: $task: command not found."
    return 1
}
