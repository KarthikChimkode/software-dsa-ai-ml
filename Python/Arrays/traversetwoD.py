import numpy as np

twoDarr = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDarr)

def traverseTDarr(array):
    for i in range(len(array)): #len(array)  covers no of rows in two dimensional array
        for j in range(len(array[0])):#len(array[0]) covers no of coloumns in array
            print(array[i][j])

traverseTDarr(twoDarr)

#fist loop will be o(mn)
#j loop will be o(n)
#print is o(1)
# so time complexity will be o(n^2)
#space is o(1) complexity