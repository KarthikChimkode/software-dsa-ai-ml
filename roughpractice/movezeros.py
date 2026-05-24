def move_zeroes(nums):
    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums

nums = [0, 1, 0, 3, 12]

print(move_zeroes(nums)) 