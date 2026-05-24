prev2 = 0
prev1 = 1



for fibo in range(18):
    newFibo = prev1 + prev2
    prev2 = prev1
    prev1 = newFibo
print(newFibo)