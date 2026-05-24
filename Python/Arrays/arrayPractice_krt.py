from array import *
#create an array and traverse.

arr1 = array('i', [1,2,3,4,5,6])

for i in arr1:
    print(i)

# 2. Access individual elements through indexes
print('Step 2')
print(arr1[5])

# 3. Append any value to the array using append() method
print('step 3')
arr1.append(7)
print(arr1)

# 4. Insert value in an array using insert() method
print('Step 4')
arr1.insert(0,0)
arr1.insert(2,11)
print(arr1)

# 5. Extend python array using extend() method
print('step 5')
my_array = array('i', [8,9,10])
arr1.extend(my_array)
print(arr1)

# 6. Add items from list into array using fromlist() method
print('step 6')
tempList = [15,16,17]
arr1.fromlist(tempList)
print(arr1)
# 7. Remove any array element using remove() method
print('stepp 7')
arr1.remove(11)
print(arr1)
# 8. Remove last array element using pop() method
print('step 8')
arr1.pop()
print(arr1)
# 9. Fetch index of any element through  using index() method
print('step 9')
print(arr1.index(15)) #here it will return the inde of element 15 from arr1(array).

# 10. Reverse a python array using reverse() method
print('step 10')
arr1.reverse()
print(arr1)
# 11. Get array buffer information through buffer_info() method
print('step 11')
"""
In Python, the buffer_info() method is a method available for objects 
created using the array module. It returns a tuple containing information 
about the underlying memory buffer used by the array. 
Specifically, it returns a tuple with two elements:

1.The address of the memory buffer (an integer).
2.The number of elements in the array."""
print(arr1.buffer_info())

# 12. Check for number of occurrences of an element using count() method
print('step 12')
arr1.append(10)
print(arr1.count(10))
print(arr1)

# 13. Convert array to string using tostring() method
print('step 13')
strTemp = arr1.tobytes()
print(strTemp)
ints = array('i')
ints.frombytes(strTemp)
print(ints)
# 14. Convert array to a python list with same elements using tolist() method
#print('step 14')
#print(arr1.tolist())
# 15. Append a string to char array using fromstring() method
print('step 15')
string = array('u',['A','B','C','D','E'])
print(string)
string_to_append ='FGH'

for ch in string_to_append:
    string.append(ch)

print(string)
print(string.tolist())

# 16. Slice Elements from an array
print("Step 16")
print(arr1[3:12])
print(arr1[3:])
print(arr1[:4])
 