n, k = (int(i) for i in input().split())
a = (int(i) for i in input().split())
res, uniq = [], set()
for i, ai in enumerate(a):
    if ai not in uniq:
        uniq.add(ai)
        res.append(i + 1)
        if len(res) >= k:
            break
if len(res) >= k:
    print("YES")
    print(*res)
else:
    print("NO")
