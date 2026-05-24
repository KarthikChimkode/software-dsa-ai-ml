from array import array
#or
#from array import * 
'''Importing everything from a module using from array import * 
can sometimes lead to namespace pollution and make it unclear 
where certain functions or classes come from. 
It's generally recommended to import only what you need from a module 
to keep your code clear and avoid potential naming conflicts. '''

arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d',[1.3,1.5,1.6])

#arr1.insert(2,9)
#print(arr1)

def transvearray(array):
    for i in array:
        print(i)

transvearray(arr1)
transvearray(arr2)
