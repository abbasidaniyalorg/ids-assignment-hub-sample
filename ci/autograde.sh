#! /bin/bash

set -e

# assignment name
assignment_name=$1

# notebook path
notebook_path=$2


if [ -z "$assignment_name" ]; then
    echo "Assignment name is missing"
    exit 1
fi

if [ -z "$notebook_path" ]; then
    echo "Notebook path is missing"
    exit 1
fi


echo "Autograding assignment: $assignment_name with notebook: $notebook_path"


# ci_student
ci_student=ci_student

# create a new ci_student
nbgrader db student add ci_student


# check if assignment name exists
nbgrader db assignment list | grep -q "$assignment_name"
# TODO: check if release!


# copy path to submission notebook to ci_student submission notebook, create directories if missing
file_path="./submitted/$ci_student/$assignment_name/"
# mkdir -p $(dirname $file_path)
mkdir -p "$file_path"


# copy notebook to ci_student submission notebook
cp "$notebook_path" "$file_path"

# autograde
nbgrader autograde "$assignment_name" --student $ci_student

# generate feedback
nbgrader generate_feedback "$assignment_name" --student $ci_student

set +e