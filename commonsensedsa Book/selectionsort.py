def selectionSort(array):
    for i in range(len(array)):
        lowest_number_index =i
        for j in range(i+1, len(array)):
            if array[j] < array[lowest_number_index]:
                lowest_number_index = j

        if lowest_number_index != i:
            temp = array[i]
            array[i] = array[lowest_number_index]
            array[lowest_number_index] = temp
    return array

print(selectionSort([4, 2, 7, 1, 3]))


"""
Debugging Walkthrough for array [4, 2, 7, 1, 3]:

Step 0: Initial array: [4, 2, 7, 1, 3]

Step 1: i = 0

lowest_number_index = 0 (value 4)

Compare with 2 → 2 < 4 → update lowest_number_index = 1

Compare with 7 → 7 > 2 → no change

Compare with 1 → 1 < 2 → update lowest_number_index = 3

Compare with 3 → 3 > 1 → no change

Swap array[0] and array[3] → [1, 2, 7, 4, 3]

Step 2: i = 1

lowest_number_index = 1 (value 2)

Compare with 7 → 7 > 2 → no change

Compare with 4 → 4 > 2 → no change

Compare with 3 → 3 > 2 → no change

No swap needed

Array stays: [1, 2, 7, 4, 3]

Step 3: i = 2

lowest_number_index = 2 (value 7)

Compare with 4 → 4 < 7 → update lowest_number_index = 3

Compare with 3 → 3 < 4 → update lowest_number_index = 4

Swap array[2] and array[4] → [1, 2, 3, 4, 7]

Step 4: i = 3

lowest_number_index = 3 (value 4)

Compare with 7 → 7 > 4 → no change

No swap needed

Array stays: [1, 2, 3, 4, 7]

Step 5: i = 4

Only one element left → already in place

Array stays: [1, 2, 3, 4, 7]

Key Points for Debugging/Revision:

The outer loop i determines the position to fill with the smallest remaining element.

lowest_number_index keeps track of the index of the minimum value in the unsorted portion.

The inner loop compares all remaining elements to find the smallest number.

If the smallest number is not already in position, a swap occurs.

After each outer loop iteration, the left portion of the array is sorted.

By the last iteration, all elements are sorted in ascending order
"""