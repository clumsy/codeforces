n, m = (int(i) for i in input().split())
map = {}
for _ in range(m):
    a, b = input().split()
    map[a] = map[b] = b if len(b) < len(a) else a
res = " ".join(map[c] for c in input().split())
print(res)
