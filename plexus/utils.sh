#!/bin/bash

# example dir /Users/rindtorff/github/labdao/diffdock/test
function_name=$1
dir=$2

# make sure the ipfs daemon is running

# if the ipfs daemon is not running, start it in a subshell

if [ "$function_name" == "check" ]; then
    # Generate the CIDv1 for the directory
    cid=$(ipfs add -r --offline --only-hash --cid-version=1 "$dir" | tail -n 1 | awk '{print $2}')
    echo "CID: $cid"

    echo "checking local and remote status..."
    # Check if the CID is identifiable from the local daemon
    local=$(ipfs block stat "$cid" | head -n 1)
    echo "local status: $local"

    # Check if the CID is identifiable from the ipfs.io gateway
    
    status=$(curl --head --silent https://sapphire-defiant-pinniped-447.mypinata.cloud/ipfs/$cid | head -n 1)
    echo "remote status: $status"
    #if echo "$status" | grep -q 404
    #    echo "file does not exist"
    #    elif echo "$status" | grep -q 200
    #    echo "file exists"
    #    else
    #    echo "error"
    #fi 
elif [ "$function_name" == "pin" ]; then
    # pin file to ipfs with CIDv1 using kubo client
    cid=$(ipfs add -r --cid-version=1 "$dir" | tail -n 1 | awk '{print $2}')
    echo "file pinned"
    echo "CID: $cid"
    echo "pinning to remote..."
    #TODO add --name="$dir" to call
    ipfs pin remote add --background --service=pinata-api "$cid"
    status=$(ipfs pin remote ls --service=pinata-api --cid="$cid" --status=queued,pinning,pinned,failed)
    echo "remote status: $status"
elif [ "$function_name" == "setup" ]; then
    # check the available pinning services and add missing ones from .env file
    echo "not yet implemented"
else
  echo "Error: Invalid function name. Use 'check', 'pin', or 'setup'."
fi
