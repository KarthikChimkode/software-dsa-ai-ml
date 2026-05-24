def contains_duplicate(nums):
    return len(nums) != len(set(nums))


print(contains_duplicate([10, 20, 30, 40, 20, 30]))
print(contains_duplicate([10, 20, 30, 40]))

