def sorting(list1):
    n = len(list1)

    for i in range(n):
        for j in range(i+1, n):
            if list1[i]>list1[j]:
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp

    print(list1)

list1 = list(map(int, input().split()))
    
sorting(list1)