def product_except_self(nums):
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(len(nums) -1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]

    return res 

print(product_except_self([10, 20, 40 ,40]))