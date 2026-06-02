#!/bin/bash

echo "Parent PID: $$"

(
    sleep 2
    echo "Child PID: $BASHPID | Parent PID: $PPID"
    echo "Child is now an orphan (parent has exited)."
) &

echo "Parent process exiting now."
exit 0

: '
Sample Output:
Parent PID: 4521
Parent process exiting now.
Child PID: 4522 | Parent PID: 1
Child is now an orphan (parent has exited).
'
