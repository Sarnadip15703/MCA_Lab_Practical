#!/bin/bash

> backup

for file in *; do
    if [ -f "$file" ]; then
        name=$file
        size=$(stat -c%s "$file")
        perms=$(stat -c%A "$file")
        echo "Name: $name  Size: $size bytes  Permissions: $perms" >> backup
    fi
done

echo "File details saved to backup:"
cat backup

: '
Sample Output:
File details saved to backup:
Name: Q1_greet.sh  Size: 215 bytes  Permissions: -rwxr-xr-x
Name: Q2_rename_lowercase.sh  Size: 189 bytes  Permissions: -rwxr-xr-x
'
