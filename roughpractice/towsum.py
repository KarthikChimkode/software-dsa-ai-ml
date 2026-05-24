def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num 
        if diff in seen:
            return [diff, num]
        seen[num] = i 
    
nums = [10, 20, 30, 90]
target = 50

print(two_sum(nums, target))