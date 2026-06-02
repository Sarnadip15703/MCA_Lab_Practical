#!/bin/bash

cat > emp_data.txt << 'EOF'
101 Alice 400 25
102 Bob 6000 30
103 Carol 1200 28
104 Dave 5500 35
105 Eve 300 22
EOF

awk '
BEGIN {
    print "This is the employee information"
    print "Todays date is : " strftime("%Y-%m-%d")
    print ""
    printf "%-10s %-10s %-10s %-5s %-12s\n", "emp no.", "name", "salary", "age", "commission"
    total_sal = 0
    total_comm = 0
    count = 0
}
{
    emp_no = $1; name = $2; salary = $3; age = $4
    if (salary < 500)
        commission = salary * 0.05
    else if (salary > 5000)
        commission = salary * 0.10
    else
        commission = 0
    printf "%-10s %-10s %-10s %-5s %-12.2f\n", emp_no, name, salary, age, commission
    total_sal += salary
    total_comm += commission
    count++
}
END {
    print ""
    print "The No. of employees is : " count
    print "The total salary is : Rs. " total_sal
    printf "The total commission is : Rs. %.2f\n", total_comm
    print "Thanking you for seeing this report."
}
' emp_data.txt

: '
Sample Output:
This is the employee information
Todays date is : 2026-05-31

emp no.    name       salary     age   commission
101        Alice      400        25    20.00
102        Bob        6000       30    600.00
103        Carol      1200       28    0.00
104        Dave       5500       35    550.00
105        Eve        300        22    15.00

The No. of employees is : 5
The total salary is : Rs. 13400
The total commission is : Rs. 1185.00
Thanking you for seeing this report.
'
