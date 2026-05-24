def two_sum(nums, k):
    seen = {}
    
    for i , num in enumerate(nums):
        diff = k - num
        if diff in seen:
            return (seen[diff], i)
        seen[num] = i 


nums = [10, 20, 40, 0, 0, 70, 5, 9, 4, 78, 67,  90]
k = 100
print(two_sum(nums, k)) 