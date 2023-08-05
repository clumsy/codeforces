from collections import defaultdict

e = defaultdict(int)
n = int(input())
for i in range(n):
    a, x = (int(i) for i in input().split())
    e[a] = x
m = int(input())
for i in range(m):
    b, y = (int(i) for i in input().split())
    e[b] = max(e.get(b, 0), y)
res = sum(e.values())
print(res)
