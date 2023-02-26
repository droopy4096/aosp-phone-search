#!/bin/bash

PATTERN_FILE=${1}
INPUT_FILE=${2}

while read p; do 
    model=${p##*: }
    agrep "${model}" ${INPUT_FILE}
done < ${PATTERN_FILE} | sort -u
