def process_data(Ist):
    for i in range(len(Ist)):
        if i % 2 == 0:  # For even indices
            Ist[i] *= 2  # Double the value
        else:           # For odd indices
            Ist[i] += 3  # Add 3 to the value
    return Ist

data = [1, 2, 3, 4, 5]
result = process_data(data)


print(result)


'''You are given a list of integers. Your task is to write a function process_data(lst) that modifies the list based on the index of each element:

If the element is at an even index (0, 2, 4, ...), double its value.

If the element is at an odd index (1, 3, 5, ...), add 3 to its value.

Return the modified list.

Example:
Input: [1, 2, 3, 4, 5]
Output: [2, 5, 6, 7, 10]
Explanation:

Index 0 → 1 × 2 = 2

Index 1 → 2 + 3 = 5

Index 2 → 3 × 2 = 6

Index 3 → 4 + 3 = 7

Index 4 → 5 × 2 = 10'''