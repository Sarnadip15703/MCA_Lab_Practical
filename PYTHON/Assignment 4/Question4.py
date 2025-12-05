# s=input("enter the number:")
# nums=s.split()
# def digit_sum(n):
#     sum=0
#     for i in n:
#         sum+=int(i)
#     return sum
s = input("Enter space separated numbers: ")

nums = s.split()

# Function to calculate digit sum
def digit_sum(n):
    return sum(int(d) for d in n)

longest = []
current = [nums[0]]

for i in range(1, len(nums)):
    if digit_sum(nums[i]) > digit_sum(nums[i-1]):
        current.append(nums[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [nums[i]]

if len(current) > len(longest):
    longest = current

print("Longest sequence:", longest)
print("Length:", len(longest))
