#! /usr/bin/env bash

function DALL-E() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == help ] ; then
        local options="brush=tiling|randomwalk,~dryrun,filename=<output.png>,lines=<5>,url,verbose"
        abcli_show_usage "DALL-E render input.txt|https://allpoetry.com/16-bit-Intel-8088-chip$ABCUL[$options]" \
            "render input -> <output.png>."
        return
    fi

    if [ "$task" == render ] ; then
        local input_filename=$2

        local options=$3
        local brush=$(abcli_option "$options" brush tiling)
        local lines=$(abcli_option "$options" lines -1)
        local verbose=$(abcli_option_int "$options" verbose 0)
        local dryrun=$(abcli_option_int "$options" dryrun 1)

        local output_filename="${input_filename##*/}"
        local output_filename=$(abcli_option "$options" filename $output_filename)

        python3 -m openai_cli.DALLE \
            render \
            --input_filename $input_filename \
            --output_filename $abcli_object_path/$output_filename \
            --brush $brush \
            --dryrun $dryrun \
            --lines $lines \
            --verbose $verbose \
            "${@:4}"

        return
    fi

    abcli_log_error "-DALLE: $task: command not found."
}