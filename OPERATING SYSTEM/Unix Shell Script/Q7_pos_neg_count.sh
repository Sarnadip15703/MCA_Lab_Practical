#!/bin/bash

pos=0
neg=0

for num in "$@"; do
    if [ $num -gt 0 ]; then
        pos=$((pos + 1))
    elif [ $num -lt 0 ]; then
        neg=$((neg + 1))
    fi
done

echo "Count of Positive Numbers: $pos"
echo "Count of Negative Numbers: $neg"

: '
Sample Input:
./Q7_pos_neg_count.sh 3 -1 5 -2 7

Sample Output:
Count of Positive Numbers: 3
Count of Negative Numbers: 2
'
