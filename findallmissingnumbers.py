nums = [1, 3, 4, 5, 6, 8, 8, 0, 2, 10]
set_nums = set(nums)

ret = []

for i in range(1, len(nums) + 1):
    if i not in set_nums:
        ret.append(i)

print(ret)
