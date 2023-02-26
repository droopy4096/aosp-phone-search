#!/bin/sh

GSM_DEVICES=${1}

python gsm_arena_devices.py "${GSM_DEVICES}" | jq -r '.[] | "\(.manufacturer): \(.model)"' | sort