#!/bin/bash
# use a passed var or current dir
workingDir="${1:$(pwd)}"
# assigned or active user
userName="${2:-$USER}"

bashLibs=$workingDir/bash
# list of system requirements to install
bashDepends=$(cat $bashLibs/depends.txt)

pythonDir=$workingDir/.venv
pythonReq=$workingDir/requirements.txt
pythonSrc=$pythonDir/bin/activate
pythonMain=$workingDir/server.py
# ignores '#' comment lines in 'requirements.txt' file
pythonDepends=$(grep -v '^\s*#' $pythonReq | sed 's/\s*#.*//' | grep -v '^\s*$')
# parent $()