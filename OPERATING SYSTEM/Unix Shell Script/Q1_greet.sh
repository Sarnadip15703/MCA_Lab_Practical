#!/bin/bash

hour=$(date +"%H")

if [ $hour -ge 5 ] && [ $hour -lt 12 ]; then
    echo "GOOD MORNING"
elif [ $hour -ge 12 ] && [ $hour -lt 17 ]; then
    echo "GOOD AFTERNOON"
elif [ $hour -ge 17 ] && [ $hour -lt 21 ]; then
    echo "GOOD EVENING"
else
    echo "GOOD NIGHT"
fi

: '
Sample Output:
GOOD MORNING
'
