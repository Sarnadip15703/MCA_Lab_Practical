#!/bin/bash

factorial() {
    local n=$1
    if [ $n -le 1 ]; then
        echo 1
    else
        prev=$(factorial $((n - 1)))
        echo $((n * prev))
    fi
}

if [ -z "$1" ]; then
    echo "Usage: ./Q14_factorial.sh <number>"
    exit 1
fi

result=$(factorial $1)
echo "Factorial of $1 is: $result"

: '
Sample Input:
./Q14_factorial.sh 5

Sample Output:
Factorial of 5 is: 120

Sample Input:
./Q14_factorial.sh 0

Sample Output:
Factorial of 0 is: 1
'
