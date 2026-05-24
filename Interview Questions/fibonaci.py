def fibonaci(n):
    num1 = 0
    num2 = 1

    series = []
    for _ in range(n):
        series.append(num1)
        temp = num1
        num1 = num2 
        num2 = num1 + num2
    return series



print(fibonaci(5))