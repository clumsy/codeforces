from itertools import islice

n, v = (int(i) for i in input().split())
res = [
    i + 1 for i in range(n) if any(v > int(k) for k in islice(input().split(), 1, None))
]
print(len(res))
print(*res)
