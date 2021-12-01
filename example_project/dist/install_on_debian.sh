#!/usr/bin/env bash
set -e
echo "*************************"
echo "Installing Example Project"
echo "*************************"
filePath=${1:-"/opt"}/example-project
echo "Installing to $filePath"
echo "Building Python virtual environment"
python3 -m venv $filePath/env
target=(example_package*.whl)
source $filePath/env/bin/activate
pip install "${target[0]}"
ln -s $filePath/env/bin/my-executable $filePath/my-executable
cp setup.yaml $filePath/setup.yaml
