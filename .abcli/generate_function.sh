#! /usr/bin/env bash

function openai_generate_function() {
    local options=$1
    local dryrun=$(abcli_option_int "$options" dryrun 1)

    local filename=$(abcli_clarify_input $2 frame)

    local prev_filename=$(abcli_clarify_input $3)

    local sentence=$4

    abcli_log "openai: generate: image: \"$sentence\" -[$prev_filename.png ${@:5}]-> $filename.png"

    local command_line="curl https://api.openai.com/v1/images/generations \
        -H 'Content-Type: application/json' \
        -H 'Authorization: Bearer $OPENAI_API_KEY' \
        -d '{
        \"prompt\": \"$sentence\",
        \"n\": 1,
        \"size\": \"1024x1024\"
        }' >> ./raw/$filename.json"

    abcli_log "⚙️  $command_line"
    if [ "$dryrun" == 1 ] ; then
        return
    fi
    eval "$command_line"

    # local image_url=$(jq ".data[0][url]" ./raw/$filename.json)
    # curl -o ./raw/$filename.png $image_url
}