#!/bin/bash
set -e

# Go to backend folder
cd $(dirname $0)/..
python3 -m unittest test_app.py
