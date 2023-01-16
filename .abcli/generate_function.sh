#! /usr/bin/env bash

function openai_generate_function() {
    local options=$1
    local dryrun=$(abcli_option_int "$options" dryrun 1)
    local height=$(abcli_option "$options" height 1024)
    local width=$(abcli_option "$options" width 1024)

    local filename=$(abcli_clarify_input $2 frame)

    local prev_filename=$(abcli_clarify_input $3)

    local sentence=$4

    abcli_log "openai: generate: image: \"$sentence\" -[$prev_filename.png ${@:5}]-> $filename.png"

    if [ -z "$prev_filename" ] ; then
        # https://beta.openai.com/docs/api-reference/images/create
        local command_line="curl https://api.openai.com/v1/images/generations \
            -H 'Content-Type: application/json' \
            -H 'Authorization: Bearer $OPENAI_API_KEY' \
            -d '{
            \"prompt\": \"$sentence\",
            \"n\": 1,
            \"size\": \"${height}x${width}\"
            }' > ./raw/$filename.json"
    else
        # https://beta.openai.com/docs/api-reference/images/create-edit?lang=curl
        local command_line="curl https://api.openai.com/v1/images/edits \
            -H 'Authorization: Bearer $OPENAI_API_KEY' \
            -F image='@./raw/$prev_filename.png' \
            -F prompt=\"$sentence\" \
            -F n=1 \
            -F size=\"${height}x${width}\" \
            > ./raw/$filename.json"
    fi

    abcli_log "⚙️  $command_line"
    if [ "$dryrun" == 1 ] ; then
        return
    fi
    eval "$command_line"

    # https://stackoverflow.com/a/44656583/17619982
    # https://cameronnokes.com/blog/working-with-json-in-bash-using-jq/
    local image_url=$(jq -r '.data[0]["url"]' ./raw/$filename.json)
    curl -o ./raw/$filename.png $image_url
}