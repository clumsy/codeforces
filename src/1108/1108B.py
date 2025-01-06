from collections import Counter


n, a = int(input()), (int(i) for i in input().split())
cnt = Counter(a)
x = max(cnt)
for i in range(1, x):
    if i * i > x:
        break
    if x % i == 0:
        vs = (i,) if i * i == x else (i, x // i)
        for v in vs:
            cnt[v] -= 1
            if cnt[v] == 0:
                del cnt[v]
y = max(cnt)
res = x, y
print(*res)
