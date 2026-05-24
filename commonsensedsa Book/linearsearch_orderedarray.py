def linear_search(array, value):

    for element in array:
        if element == value:
            return value
        
        elif element > value:
            break
    return None

print(linear_search([10, 20, 25, 40], 30))

'''the code assumes array is sorted and in acending order if element is greater then value it assumes that there is no value presents and breaks'''