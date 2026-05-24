i = 0
matrix = [[],[],[],[]]
N = 4
while i < N:
    for i in range(N):
        for j in range(N):
            if i == j:
                matrix[i][j] = N * N
            else:
                matrix[i][j] = N -j

print(matrix)