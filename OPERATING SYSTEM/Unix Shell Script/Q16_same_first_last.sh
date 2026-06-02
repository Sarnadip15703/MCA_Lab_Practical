#!/bin/bash

echo "Enter filename:"
read filename

if [ ! -f "$filename" ]; then
    echo "File '$filename' not found."
    exit 1
fi

echo "Words where first and last character are same:"
for word in $(cat "$filename"); do
    first="${word:0:1}"
    last="${word: -1}"
    if [ "$first" = "$last" ]; then
        echo "$word"
    fi
done

: '
Sample FILE content:
level radar hello civic apple noon

Sample Input:
Enter filename: FILE

Sample Output:
Words where first and last character are same:
level
radar
civic
noon
'
