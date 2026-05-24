import numpy as np

twoDarr = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDarr)

deletetwoarr = np.delete(twoDarr, 0, axis=1)
deletetwoarr1 = np.delete(twoDarr, 0, axis=0)
deletetwoarr2 = np.delete(twoDarr, 1,axis=0)
deletetwoarr3 =np.delete(twoDarr,1,axis=1)
print(deletetwoarr)
print(deletetwoarr1)
print(deletetwoarr2)
print(deletetwoarr3)
#time = o(mn)