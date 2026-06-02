#!/bin/bash

echo "Users currently logged in:"
who | awk '{print $1}'

echo ""
echo "Users that have logged out:"
last | awk '$2 ~ /pts|tty/ && /gone|still/ {print $1}' | sort -u

: '
Sample Output:
Users currently logged in:
john
alice

Users that have logged out:
bob
carol
'
