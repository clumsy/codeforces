t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    for i in range(n):
        s = input().split()
        if i == 0:
            res.extend(int(c) for c in s)
        else:
            res.append(int(s[-1]))
    res = [sum(range(1, 2 * n + 1)) - sum(res)] + res
    print(*res)
