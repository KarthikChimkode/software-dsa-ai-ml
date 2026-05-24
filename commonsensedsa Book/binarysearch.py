def binary_search(array, value):
    lower_bound = 0
    upper_bound = len(array) - 1
    
    while lower_bound <= upper_bound:
        mid = int((upper_bound + lower_bound) / 2)

        if value < array[mid]:
            upper_bound = mid - 1
        elif  value > array[mid]:
            lower_bound = mid + 1
        elif value == array[mid]:
            return mid
    return None

print(binary_search([10, 20, 25, 40], 40))

# imporved by ai
def binary_search(array, value):
    lower = 0
    upper = len(array) - 1

    while lower <= upper:
        mid = (lower + upper) // 2  # floor division for clarity

        if array[mid] == value:
            return mid
        elif value < array[mid]:
            upper = mid - 1
        else:
            lower = mid + 1

    return -1  # conventionally return -1 if not found


print(binary_search([10, 20, 25, 40], 9))
