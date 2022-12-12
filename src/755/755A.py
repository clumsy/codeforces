n = int(input())
# if n is odd => n * odd + 1 = even
# if n is even => n * (n - 2) + 1 = n^2 - 2n + 1 = (n - 1) * (n + 1)
# if n = 2 => m = 4
res = 4 if n == 2 else 3 if n & 1 == 1 else n - 2
print(res)
