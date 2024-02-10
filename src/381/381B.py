n = int(input())
a = sorted(int(i) for i in input().split())
up, dn = [], []
for i in a[::-1]:
    if not up or up[-1] != i:
        up.append(i)
    elif i != up[0] and (not dn or i != dn[-1]):
        dn.append(i)
res = up[::-1] + dn
print(len(res))
print(*res)
