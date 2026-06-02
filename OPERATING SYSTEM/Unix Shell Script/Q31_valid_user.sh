#!/bin/bash

echo "Enter username:"
read username

if grep -q "^$username:" /etc/passwd; then
    echo "$username is a valid user."
else
    echo "$username is NOT a valid user."
fi

: '
Sample Input 1:
Enter username: root

Sample Output 1:
root is a valid user.

Sample Input 2:
Enter username: ghostuser

Sample Output 2:
ghostuser is NOT a valid user.
'
