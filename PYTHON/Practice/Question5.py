nums = [1, 3, 5, 4, 2,4,8,3]
n = len(nums)
best = []

for i in range(n):
    inc = [nums[i]]
    j = i - 1
    while j >= 0 and nums[j] < inc[0]:
        inc.insert(0, nums[j])
        j -= 1

    dec = []
    j = i + 1
    while j < n and nums[j] < nums[i]:
        dec.append(nums[j])
        j += 1

    seq = inc + dec
    if len(seq) >= 3 and len(seq) > len(best):
        best = seq

print(best, len(best))