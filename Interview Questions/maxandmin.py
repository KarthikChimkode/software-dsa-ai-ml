def maxadnmin(a):
    maximum = a[0]
    minimum = a[0]

    for i in a:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    print('maximum: ', maximum)
    print('minimun: ', minimum)

def main(): #to take input of array or list and call the above function and to print the results
    a = list(map(int, input("Enter the elements that are seperated by space: ").split()))

    maxadnmin(a)
 

if __name__ == '__main__':
    main()

    

