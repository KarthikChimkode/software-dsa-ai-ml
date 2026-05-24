n = 4

for i in range(n):
    # spaces

    for j in range(n - i -1):
        print(" ", end=" ")

    # stars
    for j in range(2 * i + 1):
        print("*", end=" ")

    print()