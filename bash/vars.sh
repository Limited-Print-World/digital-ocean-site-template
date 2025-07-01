#!/bin/bash
# use a passed var or current dir
workingDir="${1:$(pwd)}"
# assigned or active user
userName="${2:-$USER}"

bashLibs=$workingDir/bash
bashDepends=$(cat $bashLibs/depends.txt)

pythonDir=$workingDir/.venv
pythonReq=$workingDir/requirements.txt
pythonSrc=$pythonDir/bin/activate
pythonMain=$workingDir/server.py

pythonDepends=$(grep -v '^\s*#' $pythonReq | sed 's/\s*#.*//' | grep -v '^\s*$')
parent $()