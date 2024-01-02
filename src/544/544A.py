k = int(input())
s = input()
uniq, res, p = set(), [], 0
for i, c in enumerate(s):
    if c not in uniq:
        uniq.add(c)
        if i > p:
            res.append(s[p:i])
        p = i
        k -= 1
    if k == 0:
        break
res.append(s[p:])
if k == 0:
    print("YES")
    print(*res, sep="\n")
else:
    print("NO")
