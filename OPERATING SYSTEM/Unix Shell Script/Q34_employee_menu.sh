#!/bin/bash

empfile="employees.txt"

if [ ! -f "$empfile" ]; then
    touch "$empfile"
fi

while true; do
    echo ""
    echo "1. Search employee by emp_no"
    echo "2. Display all emp_no and salary"
    echo "3. Append new employee record"
    echo "4. Exit"
    echo "Enter choice:"
    read choice

    case $choice in
        1)
            echo "Enter employee number to search:"
            read empno
            result=$(grep "^$empno," "$empfile")
            if [ -z "$result" ]; then
                echo "Employee not found."
            else
                echo "Record: $result"
            fi
            ;;
        2)
            echo "emp_no  salary"
            awk -F',' '{print $1, $3}' "$empfile"
            ;;
        3)
            echo "Enter emp_no:"
            read empno
            echo "Enter emp_name:"
            read empname
            echo "Enter emp_sal:"
            read empsal
            echo "$empno,$empname,$empsal" >> "$empfile"
            echo "Record added."
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid option."
            ;;
    esac
done

: '
Sample Input/Output:

Enter choice: 3
Enter emp_no: 101
Enter emp_name: Alice
Enter emp_sal: 50000
Record added.

Enter choice: 3
Enter emp_no: 102
Enter emp_name: Bob
Enter emp_sal: 60000
Record added.

Enter choice: 2
emp_no  salary
101 50000
102 60000

Enter choice: 1
Enter employee number to search: 101
Record: 101,Alice,50000

Enter choice: 4
Exiting...
'
