#!/bin/bash

echo "Program Name: $0"
echo "Arguments:"
for arg in "$@"; do
    echo "$arg"
done

: '
Sample Input:
./Q4_cmdline_args.sh one two three

Sample Output:
Program Name: ./Q4_cmdline_args.sh
Arguments:
one
two
three
'
