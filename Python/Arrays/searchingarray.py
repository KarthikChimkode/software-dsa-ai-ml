from array import array

arr1 = array('i', [1,2,3,4,5,6])

target = int(input('Enter the target element:')) # it takes input of target for our convienece 

def LinearSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return f"The index that elemnet stored in is {i}"
        
    return -1

print(LinearSearch(arr1, target))# here we are taking array as arr1 so we replaced the array with arr1 to execute