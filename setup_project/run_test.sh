#!/bin/bash
echo "Running server/team_mgmt/api_test.py file..."

cd ../server
source server_venv/bin/activate
python team_mgmt/api_test.py
