#!/bin/bash

echo "Enter username:"
read username

info=$(grep "^$username:" /etc/passwd)

if [ -z "$info" ]; then
    echo "User '$username' not found."
else
    echo "User Information:"
    echo "$info"
fi

: '
Sample Input:
Enter username: root

Sample Output:
User Information:
root:x:0:0:root:/root:/bin/bash
'
