#! /bin/bash

set -e

# notebook path
notebook_path=$1

if [ -z "$notebook_path" ]; then
    echo "Notebook path is missing"
    exit 1
fi


# echo "Validating assignment with notebook: $notebook_path"

# nbgrader validate
nbgrader validate "$notebook_path"
set +e