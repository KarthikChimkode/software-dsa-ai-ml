nums= [1 ,3, 4, 5, 6,7, 8,0,2]

nums = sorted(nums)

for i , v in enumerate(nums):
    if (i != v):
        print(v-1)
        break  
    if v == len(nums) - 1:
        print(v + 1)