n = int(input())
a = [int(input()) for _ in range(n)]
res = [i // 2 for i in a]
d = sum(res)
for i in range(n):
    if d == 0:
        break
    if a[i] & 1 == 0:
        continue
    if d > 0 and res[i] < 0:
        res[i] -= 1
        d -= 1
    elif d < 0:
        res[i] += 1
        d += 1
res = "\n".join(str(i) for i in res)
print(res)
