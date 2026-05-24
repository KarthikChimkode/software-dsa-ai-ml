#searching Two Dimensional Array
#note : this will return first occurence of array
import numpy as np

twoDarr = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDarr)

def searchTwoArr(array, value):
    for i in range(len(array)): #time o(mn)
        for j in range(len(array[0])): #time o(n)
            if array[i][j] == value: #time o(1)
                return "The value is located at index "+str(i)+" "+str(j)
    
    return "element is not found"

print(searchTwoArr(twoDarr, 18))

#time o(n^2)
#space o(1)