t = int(input())
for _ in range(t):
    n = int(input())
    # 3,-2 -> 2 if n == 1
    # 2,3 -> 1 for n = 2,3
    # n//3 for rest
    res = 2 if n == 1 else n // 3
    print(res)
