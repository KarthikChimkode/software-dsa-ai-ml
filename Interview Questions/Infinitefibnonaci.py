def infinitefibonaci():
    a = 0
    b = 1

    while True:
        yield a #if we use print here it will print infinityly even if we use print(next(f1))
        temp = a
        a = b
        b = temp+b

f1 = infinitefibonaci()
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))