#! /usr/bin/env bash

function test_openai_commands_vision() {
    local object_name=$(abcli_mlflow_tags_search \
        area=vancouver,ingest,published \
        --log 0 \
        --count 1 \
        --offset 0)

    abcli_assert "$object_name" - non-empty
    [[ $? -ne 0 ]] && return 1

    openai_commands_vision \
        - \
        Davie,Bute,.jpg \
        "list some of the things that you see in these images." \
        $object_name \
        --max_count 10 \
        --verbose 1
}
