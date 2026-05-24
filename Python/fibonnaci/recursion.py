

def fibonaci(n):
    prev1 = 1
    prev2 = 0
    while n >= 1:
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        n -= 1
    else:
        return n
    
fibonaci(18)