n = int(input())
t = (int(i) for i in input().split())
d = [[], [], []]
for i, e in enumerate(t):
    d[e - 1].append(i + 1)
res = min(len(x) for x in d)
print(res)
for i, j, k in zip(*d):
    print(i, j, k)
