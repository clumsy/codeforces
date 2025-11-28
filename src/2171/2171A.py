t = int(input())
for _ in range(t):
    n = int(input())
    res = 0 if n & 1 == 1 else n // 4 + 1
    print(res)
