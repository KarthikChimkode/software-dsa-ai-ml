from array import array

arr1 = array('i', [1,2,3,4,5])
index = int(input('Enter index number:'))

def accessELement(array, index): #array is name given to arrays that are stored and index is number or address where the stored array is
    if index >= len(array):#lenghth of array is equal to length of index that specify the arrays address
        print('There is not any element in this index')
    else:
        print(array[index]) 

accessELement(arr1, index) #array_name[array_index]

