n, b = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
d = (b + sum(a)) / n
a = [d - i for i in a]
res = [-1] if any(i < 0 for i in a) else a
print(*res, sep="\n")
