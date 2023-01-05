p, n = (int(i) for i in input().split())
x = [int(input()) for _ in range(n)]
s, res = set(), -1
for i, e in enumerate(x):
    if (e := e % p) in s:
        res = i + 1
        break
    s.add(e)
print(res)
