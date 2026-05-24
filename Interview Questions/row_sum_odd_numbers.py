'''Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8'''

def row_sum_odd_numbers(n):
    # First number in nth row = n*(n-1) + 1
    first = n * (n-1) + 1
    sum = 0
    # Each row n has n numbers
    for i in range(n):
        sum += first + (i * 2)
    return sum
   # return n ** 3


print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(3))
print(row_sum_odd_numbers(4))


'''
so here i am doing the sum of the numbers 
in the nth row of this triangle (starting at index 1)
The theory is that the first number in the nth row is n*(n-1) + 1
and the next number is the first number + (i * 2) for each number in the row

and the sum of the numbers in the nth row is n*(n-1) + 1 + (n-1)*2 + (n-2)*2 + ... + 1*2

if 1 is nth row then 1 is the first number in the row
if 2 is nth row then 3 is the first number in the row and the next number is 5
if 3 is nth row then 7 is the first number in the row and the next number is 9 and the next number is 11
if 4 is nth row then 13 is the first number in the row and the next number is 15 and the next number is 17 and the next number is 19
and so on
in form of a triangle like this:
1
3 5
7 9 11
13 15 17 19
21 23 25 27 29
and so on
or linke proper triangle like this:
       1
      3 5
    7 9 11
  13 15 17 19
21 23 25 27 29
and so on
and the sum of the numbers in the nth row is n*(n-1) + 1 + (n-1)*2 + (n-2)*2 + ... + 1*2
and the sum of the numbers in the nth row is n*(n-1) + 1 + (n-1)*2 + (n-2)*2 + ... + 1*2


'''







