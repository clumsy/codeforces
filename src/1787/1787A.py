t = int(input())
for _ in range(t):
    n = int(input())
    # n has to be even because:
    # y*x^y + x*y^x = x*y*(x^(y-1) + y^(x-1))) = n
    # if either is even -> product is even
    # if both are odd the parents has a sum of two odd numbers, hence also even
    res = [-1] if n & 1 == 1 else [1, n // 2]
    print(*res)
