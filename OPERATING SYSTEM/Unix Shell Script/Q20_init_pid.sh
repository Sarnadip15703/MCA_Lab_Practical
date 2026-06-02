#!/bin/bash

pid=$(ps -e | grep -w 'init\|systemd' | head -1 | awk '{print $1}')
echo "PID of init process: $pid"

: '
Sample Output:
PID of init process: 1
'
