#!/usr/bin/bash

#!/bin/bash
workingDir=$(pwd)

# VARS
source $workingDir/bash/vars.sh $workingDir

# FUNCS
source $workingDir/bash/funcs.sh $workingDir



message "BUILDING VENV"

python3 -m venv $pythonDir

message "ACTIVATING VENV"

source $pythonSrc

pip install -r $pythonReq

python3 $pythonMain

message "EXE IN:: $workingDir"
message "SYS DEPENDS:: $bashDepends"
message "SYS DEPENDS:: $pythonDepends"
