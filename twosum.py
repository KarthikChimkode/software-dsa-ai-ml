nums = [2, 11, 7, 3, 15]
target = 9

set_nums = set(nums)
ret = []

for i , v in enumerate(nums):
    checking = target - v
    if checking in set_nums and checking != v:
        ret.append(v)
        

print(ret)