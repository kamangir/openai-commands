#! /usr/bin/env bash

function openai_commands_generate_function() {
    local options=$1
    local dryrun=$(abcli_option_int "$options" dryrun 1)
    local height=$(abcli_option "$options" height 1024)
    local width=$(abcli_option "$options" width 1024)

    local filename=$(abcli_clarify_input $2 frame)

    local prev_filename=$(abcli_clarify_input $3)

    local prompt=$4

    if [ -z "$OPENAI_API_KEY" ]; then
        abcli_log_error "-openai_commands: generate_function: OPENAI_API_KEY is missing."
        return 1
    fi

    abcli_log "@openai: generate: image: \"$prompt\" -[$prev_filename.png ${@:5}]-> $filename.png"

    if [ -z "$prev_filename" ]; then
        # https://beta.openai.com/docs/api-reference/images/create
        local command_line="curl https://api.openai.com/v1/images/generations \
            -H 'Content-Type: application/json' \
            -H 'Authorization: Bearer $OPENAI_API_KEY' \
            -d '{
            \"prompt\": \"$prompt\",
            \"n\": 1,
            \"size\": \"${height}x${width}\"
            }' > ./raw/$filename.json"
    else
        if [ "$dryrun" == 0 ]; then
            python3 -m articraft.image \
                convert_to_RGBA \
                --source ./raw/$prev_filename.png \
                --destination ./raw/$prev_filename-RGBA.png \
                ${@:4}
        fi

        # https://beta.openai.com/docs/api-reference/images/create-edit?lang=curl
        local command_line="curl https://api.openai.com/v1/images/edits \
            -H 'Authorization: Bearer $OPENAI_API_KEY' \
            -F image='@./raw/$prev_filename-RGBA.png' \
            -F prompt=\"$prompt\" \
            -F n=1 \
            -F size=\"${height}x${width}\" \
            > ./raw/$filename.json"
    fi

    abcli_log "⚙️  $command_line"
    if [ "$dryrun" == 1 ]; then
        return
    fi
    eval "$command_line"

    # https://stackoverflow.com/a/44656583/17619982
    # https://cameronnokes.com/blog/working-with-json-in-bash-using-jq/
    local image_url=$(jq -r '.data[0]["url"]' ./raw/$filename.json)
    if [ "$image_url" == "null" ]; then
        abcli_log_error "-openai_commands: generate_function: failed: $(cat ./raw/$filename.json)"
        return 1
    fi

    echo "$prompt" >./$filename.txt

    curl -o ./raw/$filename.png $image_url
}
