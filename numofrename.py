# How many numbers are smaller tahn current number

nums = [8, 1, 2, 2, 3, ]

nums.sort()
print(nums)

res = {}

for i, v in enumerate(nums):
    
    if v not in res:
        res[v] = i
        


print(list(res.values()))

# Note :

"""
numbers get sorted 
[8, 3, 2, 2, 2, 1]

[1, 2, ,2, ,2, 3, 8] 


after sorting it goes into loop where if v or value or number in array if not there in the dictionary or set
it res[v] which is key and i which is index in array or the position where the value(v) was there in array 
now becomes value for key 

after sorting
1 because after sorting 1 comes first because it is smallest in ascending order
so 1 becomes key and 0 becomes value of 1 

why ? 
because aftersorting it is in position of 0 index

same with 2's value is 1 and you can see there is only one value smaller then 2 which is 1
so the answer for it 1

now as 2 is already in the dictionary it cannot add multiple times as we know set allows no duplicates in dict no duplicate key values
but we can see that with the loop logic it tried to add this values with it but it gets skipped or rejected 
2:2 and 2:3 not there in dict


now for 3's value becomes 4 which is 3:4
and 8:5


if we print with example in this comment the dict will be
{1:0, 2:1, 3:4, 8:5}

now check theres no values smaller then 1 so 0
only 1 is smaller then 2 so1
and with 3 there's 1, 2, 2, 2 are smaller which are 4 so 4
and with 8  there's 1, 2, 2, 2, 3, 8 so there's 5 

this is trick to calculate the numbers smaller then the value in an array using dict

Note: we can also use this method to calculate the greater then values we just need sort them decending order 
for this we can just do nums.sort(reverse=True)
"""