def bubblesort(list):
    unsorted_until_index = len(list) - 1 
    sorted = False

    while not sorted: # while sorted is true
        sorted = True 
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                 sorted = False
                 list[i] , list[i+1] = list[i+1], list[i]

        unsorted_until_index = unsorted_until_index -1

list=[65, 75, 45, 35, 25, 15, 10]
bubblesort(list)
print(list)


"""
Debugging Walkthrough for array [65, 75, 45, 35, 25, 15, 10]:

Step 0: Initial array: [65, 75, 45, 35, 25, 15, 10]

Outer Loop 1 (unsorted_until_index = 6)

Compare 65 & 75 → 65 < 75 → no swap

Compare 75 & 45 → 75 > 45 → swap → [65, 45, 75, 35, 25, 15, 10]

Compare 75 & 35 → 75 > 35 → swap → [65, 45, 35, 75, 25, 15, 10]

Compare 75 & 25 → 75 > 25 → swap → [65, 45, 35, 25, 75, 15, 10]

Compare 75 & 15 → 75 > 15 → swap → [65, 45, 35, 25, 15, 75, 10]

Compare 75 & 10 → 75 > 10 → swap → [65, 45, 35, 25, 15, 10, 75]

Largest element 75 "bubbled" to the end

Outer Loop 2 (unsorted_until_index = 5)

Compare 65 & 45 → swap → [45, 65, 35, 25, 15, 10, 75]

Compare 65 & 35 → swap → [45, 35, 65, 25, 15, 10, 75]

Compare 65 & 25 → swap → [45, 35, 25, 65, 15, 10, 75]

Compare 65 & 15 → swap → [45, 35, 25, 15, 65, 10, 75]

Compare 65 & 10 → swap → [45, 35, 25, 15, 10, 65, 75]

Outer Loop 3 (unsorted_until_index = 4)

Compare 45 & 35 → swap → [35, 45, 25, 15, 10, 65, 75]

Compare 45 & 25 → swap → [35, 25, 45, 15, 10, 65, 75]

Compare 45 & 15 → swap → [35, 25, 15, 45, 10, 65, 75]

Compare 45 & 10 → swap → [35, 25, 15, 10, 45, 65, 75]

Outer Loop 4 (unsorted_until_index = 3)

Compare 35 & 25 → swap → [25, 35, 15, 10, 45, 65, 75]

Compare 35 & 15 → swap → [25, 15, 35, 10, 45, 65, 75]

Compare 35 & 10 → swap → [25, 15, 10, 35, 45, 65, 75]

Outer Loop 5 (unsorted_until_index = 2)

Compare 25 & 15 → swap → [15, 25, 10, 35, 45, 65, 75]

Compare 25 & 10 → swap → [15, 10, 25, 35, 45, 65, 75]

Outer Loop 6 (unsorted_until_index = 1)

Compare 15 & 10 → swap → [10, 15, 25, 35, 45, 65, 75]

Outer Loop 7 (unsorted_until_index = 0)

Nothing to compare → array is sorted

Final Sorted Array: [10, 15, 25, 35, 45, 65, 75]
"""