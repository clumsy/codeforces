n, a = int(input()), (int(i) for i in input().split())
res = [0, 0, 0]
for i, e in enumerate(a):
    res[i % 3] += e
res = "chest" if res[0] == max(res) else "biceps" if res[1] == max(res) else "back"
print(res)
