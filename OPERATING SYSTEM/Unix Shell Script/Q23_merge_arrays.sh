#!/bin/bash

read_array() {
    local -n arr=$1
    echo "Enter number of elements for Array $1:"
    read n
    for (( i=0; i<n; i++ )); do
        echo "Enter element $((i+1)):"
        read val
        arr+=($val)
    done
}

merge_arrays() {
    merged=("${arr1[@]}" "${arr2[@]}")
}

arr1=()
arr2=()

read_array arr1
read_array arr2
merge_arrays

echo "Array 1   : ${arr1[@]}"
echo "Array 2   : ${arr2[@]}"
echo "Merged    : ${merged[@]}"

: '
Sample Input:
Enter number of elements for Array arr1: 3
Enter element 1: 1
Enter element 2: 2
Enter element 3: 3
Enter number of elements for Array arr2: 3
Enter element 1: 4
Enter element 2: 5
Enter element 3: 6

Sample Output:
Array 1   : 1 2 3
Array 2   : 4 5 6
Merged    : 1 2 3 4 5 6
'
