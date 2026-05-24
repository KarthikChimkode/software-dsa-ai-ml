def binary_search(nums, target):
    left, right = 0, len(nums) -1

    while left <= right:
        mid = (left + right)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1
        
    return -1


print(binary_search([10, 20,  30, 50, 40, 60, 70], 40))