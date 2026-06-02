#!/bin/bash

for file in *; do
    if [ -f "$file" ]; then
        lower=$(echo "$file" | tr '[:upper:]' '[:lower:]')
        if [ "$file" != "$lower" ]; then
            mv "$file" "$lower"
            echo "Renamed: $file -> $lower"
        fi
    fi
done

: '
Sample Output:
Renamed: HELLO.txt -> hello.txt
Renamed: WORLD.sh -> world.sh
'
