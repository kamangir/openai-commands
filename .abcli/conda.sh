#! /usr/bin/env bash

function openai_cli_conda() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ]; then
        abcli_show_usage "@openai conda create_env [~recreate]" \
            "create conda environment."
        return
    fi

    if [ "$task" == "create_env" ]; then
        local options=$2
        local do_recreate=$(abcli_option_int "$options" recreate 1)

        local environment_name=openai_cli

        if [[ "$do_recreate" == 0 ]] && [[ $(abcli_conda exists $environment_name) == 1 ]]; then
            abcli_eval - conda activate $environment_name
            return
        fi

        abcli_conda create_env name=$environment_name

        pushd $abcli_path_git/openai-cli >/dev/null
        pip3 install -r requirements.txt
        popd >/dev/null

        pip3 uninstall -y abcli

        pushd $abcli_path_git/awesome-bash-cli >/dev/null
        pip3 install -e .
        popd >/dev/null

        abcli_plugins install nbs
        abcli_plugins install aiart

        return
    fi

    abcli_log_error "-openai_cli: conda: $task: command not found."
    return 1
}
