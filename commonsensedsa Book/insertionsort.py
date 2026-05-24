def insertion_sort(array):
    # Start from the second element (index 1) because the first element is already "sorted"
    for i in range(1, len(array)):
        temp = array[i]  # store the current element to insert
        position = i

        # Shift elements in the sorted part (left side) to the right
        while position > 0 and array[position - 1] > temp:
            # Debugging: array[position - 1] is bigger than temp
            # so we move it one step to the right
            array[position] = array[position - 1]
            position -= 1  # move left in the array
        
        # Insert temp at the correct sorted position
        array[position] = temp

        # Debugging output to track array changes after each insertion
        # print(f"Step {i}: {array}")

    return array

print(insertion_sort([1, 4, 5, 6, 2, 3]))

"""
Debugging walkthrough for array [1, 4, 5, 6, 2, 3]:

Step 1: i = 1, temp = 4
- Compare with 1: 1 <= 4, so no shifting needed.
Array stays: [1, 4, 5, 6, 2, 3]

Step 2: i = 2, temp = 5
- Compare with 4: 4 <= 5, no shifting.
Array stays: [1, 4, 5, 6, 2, 3]

Step 3: i = 3, temp = 6
- Compare with 5: 5 <= 6, no shifting.
Array stays: [1, 4, 5, 6, 2, 3]

Step 4: i = 4, temp = 2
- Compare with 6: 6 > 2 → shift 6 right
- Compare with 5: 5 > 2 → shift 5 right
- Compare with 4: 4 > 2 → shift 4 right
- Compare with 1: 1 <= 2 → stop shifting
Insert 2 at position 1
Array becomes: [1, 2, 4, 5, 6, 3]

Step 5: i = 5, temp = 3
- Compare with 6: 6 > 3 → shift 6 right
- Compare with 5: 5 > 3 → shift 5 right
- Compare with 4: 4 > 3 → shift 4 right
- Compare with 2: 2 <= 3 → stop shifting
Insert 3 at position 2
Array becomes: [1, 2, 3, 4, 5, 6]

Final sorted array: [1, 2, 3, 4, 5, 6]
"""
 


