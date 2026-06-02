#!/bin/bash

echo "Enter text (press Ctrl+D to end):"
input=$(cat)

lines=$(echo "$input" | wc -l)
words=$(echo "$input" | wc -w)

echo "Number of Lines: $lines"
echo "Number of Words: $words"

: '
Sample Input:
Hello World
This is a test

Sample Output:
Number of Lines: 2
Number of Words: 6
'
