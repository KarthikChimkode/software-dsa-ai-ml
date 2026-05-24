import numpy as np #instead of importing array we import numby becuase numpy works best in two dimensional arrays 

twoDarr = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDarr)

#if we create two dimensional arrays like as above 
#Time complexity will be o(mn) where 'm' in numbers of colums and 'n' is number of rows
#Its time consuming and space complexity is o(mn) because we have m number of coloums and n nubmber of rows