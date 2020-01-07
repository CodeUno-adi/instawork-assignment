#!/bin/bash

# if abs_python_path not supplied at the command prompt
# display usage message and die
[ $# -eq 0 ] && { echo "Usage: $0 abs_path_to_python3_executable"; exit 1; }

echo "Creating virtualenv with python path as $1"

cd ../server

virtualenv server_venv -p $1
source server_venv/bin/activate

echo -e "\nInstall python packages..."
pip install -r requirements.txt

echo -e "\nInstalled Django version is "
python -m django --version
