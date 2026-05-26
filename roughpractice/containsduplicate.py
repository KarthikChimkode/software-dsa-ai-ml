def contains_duplicate(nums):
    return len(nums) != len(set(nums))



#brute force
def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


#Optimal seach
def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)
    
    return False
    
print(contains_duplicate([10, 20, 30, 40, 20, 30]))
print(contains_duplicate([10, 20, 30, 40]))