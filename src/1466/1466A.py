t = int(input())
for _ in range(t):
    n, x = int(input()), [int(i) for i in input().split()]
    res = set()
    for i in range(n):
        for j in range(n):
            if i != j:
                res.add(abs(x[i] - x[j]))
    res = len(res)
    print(res)
