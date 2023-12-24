n = int(input())
mins, maxs = [0] * 3, [0] * 3
for i in range(3):
    mins[i], maxs[i] = (int(i) for i in input().split())
res = [mins[i] for i in range(3)]
n -= sum(res)
for i in range(3):
    d = max(0, min(n, maxs[i] - mins[i]))
    res[i] += d
    n -= d
print(*res)
