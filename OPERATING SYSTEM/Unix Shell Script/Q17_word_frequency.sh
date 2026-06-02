#!/bin/bash

echo "Enter filename (MATTER):"
read filename

if [ ! -f "$filename" ]; then
    echo "File '$filename' not found."
    exit 1
fi

awk '
{
    for (i = 1; i <= NF; i++) {
        word = tolower($i)
        gsub(/[^a-z]/, "", word)
        if (word != "") freq[word]++
    }
}
END {
    print "Words with frequency 5 or more:"
    for (w in freq) {
        if (freq[w] >= 5)
            print w, freq[w]
    }
}
' "$filename"

: '
Sample Input:
Enter filename: MATTER

Sample Output:
Words with frequency 5 or more:
the 8
is 6
a 5
'
