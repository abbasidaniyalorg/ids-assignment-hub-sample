#! /bin/bash

set -e

# notebook path
notebook_path=$1

if [ -z "$notebook_path" ]; then
    echo "Notebook path is missing"
    exit 1
fi

set +e

# nbgrader validate
nbgrader validate "$notebook_path"
