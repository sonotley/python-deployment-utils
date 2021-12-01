#!/usr/bin/env bash
set -e
echo "*************************"
echo "Installing VMS Mimic Service"
echo "*************************"
filePath=${1:-"/opt"}/vms-mimic-service
echo "Installing to $filePath"
echo "Building Python virtual environment"
python3 -m venv $filePath/env
target=(vms_mimic_service*.whl)
source $filePath/env/bin/activate
pip install "${target[0]}"
ln -s $filePath/env/bin/vms-mimic-service $filePath/vms-mimic-service
cp -R fonts $filePath/fonts
cp -R graphics $filePath/graphics
cp setup.yaml $filePath/setup.yaml
