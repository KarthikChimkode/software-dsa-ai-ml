def max_subarray(nums):
    current = nums[0]
    maximum = nums[0]

    for num in nums[1:]:
        current = max(num, current+num)
        maximum = max(maximum, current)
    
    return maximum 

print(max_subarray([1, 2, 3, -2, 5]))