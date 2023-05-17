t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    p = (int(i) for i in input().split())
    age = [i + 1 for i in range(n - 1, -1, -1)]
    sub, new = {}, set()
    for i, e in enumerate(p):
        if e not in new:
            sub[len(sub)] = i + 1
            new.add(e)
    res = (-1 if n - i > len(sub) else sub[n - i - 1] for i in range(n))
    print(*res)
