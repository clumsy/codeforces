q = int(input())
for _ in range(q):
    n = int(input())
    res = 2 if n == 2 else n & 1
    print(res)
