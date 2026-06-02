#!/bin/bash

echo "Enter a sentence:"
read sentence

count=$(echo "$sentence" | tr -cd ' ' | wc -c)
echo "Number of blanks: $count"

: '
Sample Input:
Enter a sentence: hello world how are you

Sample Output:
Number of blanks: 4
'
