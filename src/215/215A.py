n, a = int(input()), sorted(int(i) for i in input().split())
m, b = int(input()), sorted((int(i) for i in input().split()), reverse=True)
res = ma = 0
for bi in b:
    for ai in a:
        ratio = bi // ai
        if ratio * ai == bi and ratio >= ma:
            res = res + 1 if ratio == ma else 1
            ma = ratio
print(res)
