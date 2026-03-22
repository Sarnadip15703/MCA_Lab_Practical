<<<<<<< HEAD
arr = [1, 2, 1, 3, 4, 5, 4, 3, 2, 1, 0]

longest = []

for i in range(len(arr)):
    for j in range(i+2, len(arr)):
        sub = arr[i:j+1]
        peak = sub.index(max(sub))

        if peak == 0 or peak == len(sub)-1:
            continue

        # increasing
        inc = True
        for k in range(peak):
            if sub[k] >= sub[k+1]:
                inc = False
                break

        # decreasing
        dec = True
        for k in range(peak, len(sub)-1):
            if sub[k] <= sub[k+1]:
                dec = False
                break

        if inc and dec:
            if len(sub) > len(longest):
                longest = sub

if longest:
    print("Length:", len(longest))
    print("Subsequence:", longest)
else:
    print("None")
=======
arr = [1, 2, 1, 3, 4, 5, 4, 3, 2, 1, 0]

longest = []

for i in range(len(arr)):
    for j in range(i+2, len(arr)):
        sub = arr[i:j+1]
        peak = sub.index(max(sub))

        if peak == 0 or peak == len(sub)-1:
            continue

        # increasing
        inc = True
        for k in range(peak):
            if sub[k] >= sub[k+1]:
                inc = False
                break

        # decreasing
        dec = True
        for k in range(peak, len(sub)-1):
            if sub[k] <= sub[k+1]:
                dec = False
                break

        if inc and dec:
            if len(sub) > len(longest):
                longest = sub

if longest:
    print("Length:", len(longest))
    print("Subsequence:", longest)
else:
    print("None")
>>>>>>> 8913657cbcce6a57d2b5320a18186e479137bfab
    