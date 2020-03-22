#!/bin/bash

echo "Setting up..."
cwd="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "Found cwd $cwd"

# Create path to go back to
here=$(pwd)

# change to correct directory
cd "$cwd/.." || exit

# Zip and move
zip lambda.zip src/*.py
mv lambda.zip "$cwd/../dist"

# Go back
cd "$here" || exit

echo "Done"
