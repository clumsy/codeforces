n, k = (int(i) for i in input().split())
a = sorted((int(i) for i in input().split()), reverse=True)
for i in a:
    if k % i == 0:
        res = k // i
        break
print(res)
