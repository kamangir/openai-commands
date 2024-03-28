#! /usr/bin/env bash

export VISUALYZE_URL=http://127.0.0.1:5000/

function VisuaLyze() {
    openai_cli_VisuaLyze "$@"
}

function openai_cli_VisuaLyze() {
    local task=$1

    if [[ "$task" == help ]]; then
        openai_cli_VisuaLyze browse "$@"
        openai_cli_VisuaLyze run "$@"
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

        abcli_browse_url $VISUALYZE_URL
        return
    fi

    if [[ "$task" == run ]]; then
        if [ $(abcli_option_int "$options" help 0) == 1 ]; then
            local options="dryrun"
            abcli_show_usage "VisuaLyze run$ABCUL[$options]$ABCUL[-|<object-name>]" \
                "run VisuaLyze."
            return
        fi

        export FLASK_APP=VisuaLyze.py

        abcli_eval \
            path=$abcli_path_git/openai-cli/openai_cli/VisuaLyze/flask/,$options \
            flask run
        return
    fi

    abcli_log_error "-@openai: VisuaLyze: $task: command not found."
}
