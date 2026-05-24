#Add digits until it gets single digit

def addDigits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

number = int(input("Enter a Number:\n"))
results = addDigits(number)
print(results)
