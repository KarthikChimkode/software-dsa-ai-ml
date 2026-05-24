import numpy as np

twoDarr = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDarr)
print(twoDarr.shape)

newTwoDarr = np.insert(twoDarr, 0, [[1,2,3,4]], axis=1) #here  in np.insert() we are giving name of the variable in which we want to insert arrays and position and axis determines wheather it is rows or coloums for rows we give 0 and for coloumn we give 1 in axis 
print(newTwoDarr)

newTwoDarr1 = np.insert(twoDarr, 0, [[1,2,3,4]], axis=0) 
print(newTwoDarr1)

newTwoDarr2 = np.insert(twoDarr, 1, [[1,2,3,4]], axis=1) 
print(newTwoDarr2)

newTwoDarr3 = np.insert(twoDarr, 1, [[1,2,3,4]], axis=0) 
print(newTwoDarr3)

newTwoDarr4 = np.append(twoDarr, [[1,2,3,4]], axis=0) #append function rows
print(newTwoDarr4)

