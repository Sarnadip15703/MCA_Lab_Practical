#!/bin/bash

echo "Enter choice (1-6):"
echo "1. List files in current directory"
echo "2. Current date"
echo "3. Process status"
echo "4. All current users"
echo "5. Present working directory"
echo "6. Exit"
read choice

case $choice in
    1) ls ;;
    2) date ;;
    3) ps ;;
    4) who ;;
    5) pwd ;;
    6) echo "Exiting..."; exit 0 ;;
    *) echo "Invalid option"; exit 1 ;;
esac

: '
Sample Input 1:
Enter choice: 2

Sample Output 1:
Sun May 31 10:45:00 IST 2026

Sample Input 2:
Enter choice: 5

Sample Output 2:
/home/student/ShellAssignment

Sample Input 3:
Enter choice: 9

Sample Output 3:
Invalid option
'
