#!/bin/bash

echo "Enter number of elements:"
read n

arr=()
for (( i=0; i<n; i++ )); do
    echo "Enter element $((i+1)):"
    read val
    arr+=($val)
done

sum=0
for elem in "${arr[@]}"; do
    sum=$((sum + elem))
done

echo "Array Elements: ${arr[@]}"
echo "Sum of all elements: $sum"

: '
Sample Input:
Enter number of elements: 4
Enter element 1: 10
Enter element 2: 20
Enter element 3: 30
Enter element 4: 40

Sample Output:
Array Elements: 10 20 30 40
Sum of all elements: 100
'
