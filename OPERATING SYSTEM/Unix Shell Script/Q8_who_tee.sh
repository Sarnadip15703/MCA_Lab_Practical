#!/bin/bash

who | tee who_output.txt

: '
Sample Output:
john     pts/0        2026-05-31 10:23 (:0)
alice    pts/1        2026-05-31 11:05 (:0)

(Same output is saved to who_output.txt)
'
