# Finding The nth Fibonacci Number Using Recursion

# f(n) = f(n-1) + f(n-2)

def F(n):
    if n <= 1:
        return n
    return F(n - 2) - F(n - 1)  
    
print(F(0))
