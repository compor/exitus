#!/usr/bin/env bash

[[ -z $1 ]] && echo "missing source file" && exit 1
SOURCE_FILE=$1

clang-6.0 -g -O2 -S -emit-llvm ${SOURCE_FILE} -I/llvm/tools/clang/lib/Headers/

