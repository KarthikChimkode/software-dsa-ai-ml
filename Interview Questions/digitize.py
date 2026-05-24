# Given a non-negative integer, return an array / a list of the digits in the number.

def digitize(n):
    result = []
    if n == 0:
        result.append(0)
    else:
        while n > 0:
            # n % 10 gets the rightmost digit by taking remainder when divided by 10
            # Example: 123 % 10 = 3, 45 % 10 = 5
            result.append(n % 10)
            
            # n // 10 removes the rightmost digit by integer division with 10
            # Example: 123 // 10 = 12, 45 // 10 = 4
            n = n // 10

    return result

print(digitize(12345))