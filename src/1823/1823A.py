t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = None
    for i in range(n // 2 + 1):
        s1 = i * (i - 1) // 2 if i > 1 else 0
        s2 = (n - i) * (n - i - 1) // 2 if n - i > 1 else 0
        if s1 + s2 == k:
            res = [1] * i + [-1] * (n - i)
            break
    if res is None:
        print("NO")
    else:
        print("YES")
        print(*res)
