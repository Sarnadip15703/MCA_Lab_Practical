#!/bin/bash

who | awk '{print $1}' > logged_in_users.txt
echo "Logged in users saved to logged_in_users.txt:"
cat logged_in_users.txt

: '
Sample Output:
Logged in users saved to logged_in_users.txt:
john
alice
bob
'
