n = int(input())
# NOT 4*x=n => x != n/4
# 2*x + 2*x = n => x = n/2 - y => x = [1, n/2), due to symmetry x = [1, n/4)
res = 0 if n & 1 == 1 else ((n + 3) // 4 - 1)
print(res)
