#!/bin/bash

dir=$1

if [ -z "$dir" ]; then
    echo "Usage: ./Q12_lower.sh <directory>"
    exit 1
fi

for file in "$dir"/*; do
    if [ -f "$file" ]; then
        base=$(basename "$file")
        lower=$(echo "$base" | tr '[:upper:]' '[:lower:]')
        dest="$dir/$lower"
        if [ "$base" = "$lower" ]; then
            continue
        fi
        if [ -e "$dest" ]; then
            echo "Warning: Not overwriting $lower"
        else
            mv "$file" "$dest"
            echo "Renamed: $base -> $lower"
        fi
    fi
done

: '
Sample Input:
$ ls dir/
One-File  TWO-File  Three-FILE  one-file

$ ./Q12_lower.sh dir/

Sample Output:
Warning: Not overwriting one-file
Renamed: TWO-File -> two-file
Renamed: Three-FILE -> three-file

$ ls dir/
one-file  three-file  two-file
'
