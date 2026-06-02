#!/bin/bash

for cfile in *.c; do
    if [ -f "$cfile" ]; then
        output="${cfile%.c}"
        echo "Compiling: $cfile"
        gcc "$cfile" -o "$output"
        if [ $? -eq 0 ]; then
            echo "Running: $output"
            ./"$output"
        else
            echo "Compilation failed for $cfile"
        fi
    fi
done

: '
Sample Output:
Compiling: hello.c
Running: hello
Hello, World!
Compiling: add.c
Running: add
Sum = 15
'
