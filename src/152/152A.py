n, m = (int(i) for i in input().split())
grades = [input() for _ in range(n)]
res = set()
for subj in zip(*grades):
    ma = max(subj)
    for i, g in enumerate(subj):
        if g == ma:
            res.add(i)
res = len(res)
print(res)
