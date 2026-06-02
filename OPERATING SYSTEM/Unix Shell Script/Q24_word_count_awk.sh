#!/bin/bash

echo "Enter the word to search:"
read word
echo "Enter the filename:"
read filename

if [ ! -f "$filename" ]; then
    echo "File '$filename' not found."
    exit 1
fi

awk -v w="$word" '
{
    for (i = 1; i <= NF; i++) {
        if ($i == w) count++
    }
}
END {
    print "Number of occurrences of \"" w "\" : " count+0
}
' "$filename"

: '
Sample Input:
Enter the word to search: the
Enter the filename: story.txt

Sample Output:
Number of occurrences of "the" : 7
'
