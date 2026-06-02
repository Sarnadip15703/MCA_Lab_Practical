#!/bin/bash

find / -name "*.tmp" -atime +15 -exec rm -f {} \;
echo "Deleted all .tmp files not accessed in the last 15 days."

: '
Sample Output:
Deleted all .tmp files not accessed in the last 15 days.
'
