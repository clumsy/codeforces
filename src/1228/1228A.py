l, r = (int(i) for i in input().split())
res = next((x for x in range(l, r + 1) if len(set(str(x))) == len(str(x))), -1)
print(res)
