#!/usr/bin/env bash

echo "enter the directory(format is ../workspace/the_current_project, but you only input the_current_project or workspace/the_current_project): "
read dir # input directory
dir_name=$(dirname $dir)
project_name=$(basename $dir)

function juageInteractionMode(){
    if [[ $1 == "\\" || $1 == "." ]];then
        return 1; # the relative path mode
    fi
    return 0; # the absolute path mode
}

echo -n "enter the start date(format is xxxx-xx-xx): "
read start_date # input start date

if [[ ! -d "./out" ]];then
    mkdir ./out
fi

root_name="$(dirname $(dirname $(pwd)))" # the parent directory of the current workspace
juageInteractionMode $dir_name
mode=$? # 1: relative mode otherwise absolute mode
project="" # the current project directory
if [[ $mode == 1 ]];then
    project="${root_name}/$(basename $(dirname $(pwd)))/${project_name}"
else
    project="${root_name}/${dir}"
fi
out_name="" # the current project statistics output directory.

if [[ ! -z $dir ]]; then
    if [[ ! -z $start_date ]]; then
        out_name="`pwd`/out/statistics_${project_name}_${start_date}_$(date "+%Y-%m-%d_%H%M%S")"
        mkdir -p $out_name
        echo -e "\n the current project directory:\n $project"
        echo -e "\n the current out directory:\n $out_name"
        echo -e "\n"
        python2 gitstats -c start_date=${start_date} ${project} ${out_name}
    else
        out_name="`pwd`/out/statistics_${project_name}_$(date "+%Y-%m-%d_%H%M%S")"
        mkdir -p $out_name
        echo -e "\n the current project directory:\n $project"
        echo -e "\n the current out directory:\n $out_name"
        echo -e "\n"
        python2 gitstats -c ${project} ${out_name}
    fi
else
    echo "the current project directory: $project"
    echo "the current out directory: $out_name"
    echo "the directory is not vaild."
fi
exit 0

