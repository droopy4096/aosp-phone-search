#!/bin/sh

LOS_DEVICES=${1}

python los_device_list.py "${LOS_DEVICES}" | jq -r '.[] | "\(.manufacturer): \(.model)"' | sort