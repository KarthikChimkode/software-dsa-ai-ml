def tribonacci(signature, n):
    if n <= 3:
        return signature[:n]
    result = signature.copy()
    for i in range(3, n):
        result.append(result[i-1] + result[i-2] + result[i-3])
    return result

#test
print(tribonacci([1, 1, 1], 10))
print(tribonacci([0, 0, 1], 10))
print(tribonacci([1, 2, 3], 10))
print(tribonacci([1, 1, 1], 1))