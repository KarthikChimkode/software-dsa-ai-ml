def spiralMatrix(matrix):
    ret = []

    while matrix:
        ret+= matrix.pop(0)

        if matrix and matrix[0]:
            for row in matrix:
                ret.append(row.pop()) # Note pop returns last element of the row or array 
        '''After doing ret+=matrix.pop(0) which pops out first row and appends it to ret and which leaves with 
        [[4,5,6], [7,8,9]] and we pop last item from each row and append it to s'''

        if matrix:
            ret+=matrix.pop()[::-1]

        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ret.append(row.pop(0))

    return ret

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(spiralMatrix(matrix))
