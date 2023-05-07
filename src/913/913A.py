from math import log2

n, m = (int(input()) for _ in range(2))
k = log2(m)
res = m if n > k else m % (2**n)
print(res)
