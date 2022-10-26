#!/bin/bash
now="$(date)"
printf "Started at time %s\n" "$now"
hey -n 1000 -m POST -t 0 -T "application/json" -d '[{"battery_percentage": "45","mobile_make_model": "iphonexr", "os_version": "mac_os_sierra","mac_id": "123123","latitude": "19.0536003,", "longitude": "73.0828037", "timestamp": "2022-10-20T15:58:44.767594+05:30"}]' http://localhost:8000/api/v1/metrics/bulk/
now="$(date)"
printf "ended at time %s\n" "$now"
