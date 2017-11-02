#!/usr/bin/env bash

[[ -z $1 ]] && echo "missing max number of entries" && exit 1
ENTRIES=$1

[[ -z $2 ]] && echo "missing report file location" && exit 1
REPORT_FILE=$2

awk -v N=$ENTRIES '{ a[$i]=1; next; } END{ for(i=2; i<N; i+=4) if(a[i]) print 1; else print 0; }' "$REPORT_FILE"

