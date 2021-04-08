#!/bin/bash
# script display the size body
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
