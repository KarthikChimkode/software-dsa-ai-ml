# Sure! Here's a clear and well-structured **Python coding question** based on the logic you've implemented:

# ---

# ### 🧩 **Matrix Transformation Problem**

# **Problem Statement:**

# You are given an integer `N`, representing the size of an `N x N` matrix. Fill the matrix with increasing integers starting from 1, row by row (left to right).

# **Your task is to transform the matrix as follows:**

# 1. If the row index `i` is **even** (i.e., 0, 2, 4,...), **reverse the entire row**.
# 2. After any reversal, for every element where the **row index equals the column index (`i == j`)**, **square the element** at that position.

# **Finally**, return the resulting matrix.

# ---

# ### 🧪 **Input:**

# * A single integer `N` (1 ≤ N ≤ 100) — the size of the matrix.

# ---

# ### 📤 **Output:**

# * Return the final matrix as a list of lists.

# ---

# ### 📘 **Example:**

# **Input:**

# ```
# N = 4
# ```

# **Output:**

# ```
# [[16, 3, 2, 1],
#  [5, 36, 7, 8],
#  [9, 10, 121, 12],
#  [13, 14, 15, 256]]
# ```

# ---

# ### 🧠 **Explanation:**

# * Fill matrix from 1 to 16:

#   ```
#   [1, 2, 3, 4]
#   [5, 6, 7, 8]
#   [9,10,11,12]
#   [13,14,15,16]
#   ```

# * Reverse even-indexed rows (0 and 2):

#   ```
#   [4, 3, 2, 1]
#   [5, 6, 7, 8]
#   [12,11,10,9]
#   [13,14,15,16]
#   ```

# * Square diagonal elements (i == j):

#   ```
#   [16, 3, 2, 1]
#   [5, 36, 7, 8]
#   [12, 11, 100, 9]
#   [13, 14, 15, 256]
#   ```

# Let me know if you'd like a variation using descending numbers or diagonals from other directions!

def fill_matrix(N):
    matrix = []
    value = 1

    for i in range(N):
        row = []
        for j in range(N):
            row.append(value)
            value += 1

        if i % 2 == 0:
            row.reverse()
        
        for j in range(N):
            if i == j:
                row[j] = row[j] ** 2
        
        matrix.append(row)
      
    return matrix

N = 4
result = fill_matrix(N)
for row in result:
    print(row)

