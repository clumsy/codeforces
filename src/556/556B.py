n = int(input())
a = (int(i) for i in input().split())
res = "YES"
for i, e in enumerate(a):
    if i == 0:
        rot = n - e
    e = (e - rot if i & 1 == 1 else e + rot) % n
    if e != i:
        res = "NO"
        break
print(res)
