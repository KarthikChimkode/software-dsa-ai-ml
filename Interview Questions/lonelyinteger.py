# Given an array of integers, where all elements but one occur twice, find the unique element.


"""Note : Both the lonelyinteger and lonelyinteger2 functions work if only the array elements appear twice if more than that 
 the output will be not correct"""

def lonelyinteger(a):
    b = sorted(a) #sort the array first
    for i in range(0,len(b)-1, 2): #loop from range 0 to size of array and 
        if b[i] != b[i+1]:
            return b[i]
    return b[-1]

def lonelyinteger2(a):
    unique_element = 0
    for num in a:
        unique_element ^= num
    return unique_element


def main(): #to take input of arraya and call the above function and to print the results
    a = list(map(int, input("Enter the elements that are seperated by space: ").split())) 

    result = lonelyinteger(a)

    result1 = lonelyinteger2(a)

    print(result)
    print(result1)

if __name__ == '__main__':
    main()


