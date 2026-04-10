#!/usr/bin/env bash

if [ ! -f "../README.md" ]; then
    echo "File is missing"
    exit 1
else
    echo "File exists"
fi