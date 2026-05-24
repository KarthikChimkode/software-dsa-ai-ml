'''note : index starts from '0' and so the coloums
rows are - and coloums are |
len(array)  covers no of rows in two dimensional array
len(array[0]) covers no of coloumns in array'''
import numpy as np

twoDarr = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]]) 
print(twoDarr)

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]): #if we use and we will get error for out of bound index to get incorrect index as result we need to use OR
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])

accessElements(twoDarr, 4,3)

#time o(1)
#space o(1)
