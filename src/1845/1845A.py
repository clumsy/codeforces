t = int(input())
for _ in range(t):
    n, k, x = (int(i) for i in input().split())
    res = []
    if x != 1:
        res = [1] * n
    elif k > 1:
        if n & 1 == 0:
            res = [2] * (n // 2)
        elif k > 2:
            res = [3] + [2] * (n // 2 - 1)
    if not res:
        print("NO")
    else:
        print("YES")
        print(len(res))
        print(*res)
