#!/bin/bash

echo "Enter first filename:"
read file1
echo "Enter second filename:"
read file2
echo "Enter name for merged output file:"
read outfile

if [ ! -f "$file1" ]; then
    echo "File '$file1' not found."
    exit 1
fi
if [ ! -f "$file2" ]; then
    echo "File '$file2' not found."
    exit 1
fi

sort "$file1" -o "$file1"
sort "$file2" -o "$file2"

cat "$file1" "$file2" | sort > "$outfile"

echo "Merged and sorted content written to '$outfile':"
cat "$outfile"

: '
Sample Input:
Enter first filename: file1.txt
Enter second filename: file2.txt
Enter name for merged output file: merged.txt

file1.txt content:
banana
apple

file2.txt content:
mango
cherry

Sample Output:
Merged and sorted content written to merged.txt:
apple
banana
cherry
mango
'
