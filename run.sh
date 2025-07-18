#!/usr/bin/bash
# a safer way to exe prog under default user profile/.
## Bootstrap file
# Collection of things to add in with some build setup
# and file/folder checkers

workingDir=$(pwd)


# VARS
## collection of vital system file referances
## sort of ensures all refs are localy sourced
source $workingDir/bash/vars.sh $workingDir

# FUNCS
## Collection of 
source $workingDir/bash/funcs.sh $workingDir

message "BUILDING VENV"

python3 -m venv $pythonDir

message "ACTIVATING VENV"

source $pythonSrc

message "INSTALLING VENV DEPENDENCIES"

pip install -r $pythonReq

# python3 $pythonMain
uvicorn server:app --host 0.0.0.0 --port 8080 --reload

message "EXE IN:: $workingDir"
message "SYS_DEPENDS:: $bashDepends"
message "PYTHON_DEPENDS:: $pythonDepends"
