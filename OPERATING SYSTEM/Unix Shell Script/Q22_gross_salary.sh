#!/bin/bash

echo "Enter basic salary:"
read basic

if [ $basic -lt 1500 ]; then
    hra=$(echo "$basic * 0.10" | bc)
    da=$(echo "$basic * 0.90" | bc)
else
    hra=500
    da=$(echo "$basic * 0.98" | bc)
fi

gross=$(echo "$basic + $hra + $da" | bc)

echo "Basic Salary : Rs.$basic"
echo "HRA          : Rs.$hra"
echo "DA           : Rs.$da"
echo "Gross Salary : Rs.$gross"

: '
Sample Input 1:
Enter basic salary: 1000

Sample Output 1:
Basic Salary : Rs.1000
HRA          : Rs.100
DA           : Rs.900
Gross Salary : Rs.2000

Sample Input 2:
Enter basic salary: 2000

Sample Output 2:
Basic Salary : Rs.2000
HRA          : Rs.500
DA           : Rs.1960
Gross Salary : Rs.4460
'
