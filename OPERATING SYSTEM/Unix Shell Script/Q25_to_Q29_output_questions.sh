#!/bin/bash

echo "===== Q25 ====="
a="*"
b=a
echo $b

echo "===== Q26 ====="
a=*
echo $a
echo "a"

echo "===== Q27 ====="
echo $$

echo "===== Q28 ====="
IFS=+
set economists+are+seldom+right
echo $3 $4 $#

echo "===== Q29 ====="
a=b
b=c=d=c
echo $$b
echo $$$d

: '
Sample Output:

===== Q25 =====
a

===== Q26 =====
Q1_greet.sh Q2_rename_lowercase.sh Q3_count_lines_words.sh ...
(lists all files in current directory due to glob expansion)
a

===== Q27 =====
4821
(PID of the current shell process)

===== Q28 =====
seldom right 4

===== Q29 =====
4821b
4821
(where 4821 is the PID of the current shell)
'
