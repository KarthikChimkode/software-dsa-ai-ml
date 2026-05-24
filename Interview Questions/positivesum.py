def positive_sum(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num

    return total


arr = [1, 2, 3, -4, 5]

print(positive_sum(arr))