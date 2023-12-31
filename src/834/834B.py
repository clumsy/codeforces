n, k = (int(i) for i in input().split())
s = input()
last = {c: i for i, c in enumerate(s)}
open = set()
res = "NO"
for i, c in enumerate(s):
    open.add(c)
    if len(open) > k:
        res = "YES"
        break
    if last[c] == i:
        open.remove(c)
print(res)
