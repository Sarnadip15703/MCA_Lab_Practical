#!/bin/bash

sort < IN > OUT
echo "Sorted output written to OUT."

: '
Sample IN file content:
banana
apple
cherry
mango

Sample Output:
Sorted output written to OUT.

OUT file content:
apple
banana
cherry
mango
'
