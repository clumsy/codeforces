n, d = int(input()), [int(i) for i in input().split()]
s, t = (int(i) for i in input().split())
s, t = min(s, t), max(s, t)
res = min(sum(d[s - 1 : t - 1]), sum(d[: s - 1]) + sum(d[t - 1 :]))
print(res)
