source $1/bash/vars.sh $1

pushGit(){
    git add . && git commit -m "${1:-"default value"}" && git push
}
separator-x() {
    
    # 8 #'s or whatever number it's given
    local x="${1:-8}"
    local separator=""
    for ((i=0; i<x; i++)); do
        separator="$separator#"
    done
    echo "$separator"
}

message(){
    echo $1
    separator-x 16

}
launch_api(){
    $workingDir/run_api.sh
}
launch_web(){
    $workingDir/run_api.sh
}