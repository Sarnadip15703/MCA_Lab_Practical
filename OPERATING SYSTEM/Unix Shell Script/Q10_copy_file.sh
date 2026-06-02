#!/bin/bash

echo "Enter source filename:"
read src
echo "Enter destination filename:"
read dest

if [ ! -f "$src" ]; then
    echo "Source file '$src' does not exist."
    exit 1
fi

cp "$src" "$dest"
echo "Content copied from '$src' to '$dest'."

: '
Sample Input:
Enter source filename: file1.txt
Enter destination filename: file2.txt

Sample Output:
Content copied from file1.txt to file2.txt.
'
