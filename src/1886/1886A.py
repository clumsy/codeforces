t = int(input())
for _ in range(t):
    n = int(input())
    res = None
    for i in range(2, n // 2):
        if i % 3 != 0 and (n - i - 1) % 3 != 0:
            res = [1, i, n - i - 1]
            break
    if res:
        print("YES")
        print(*res)
    else:
        print("NO")
