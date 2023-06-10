n, a = int(input()), sorted(int(i) for i in input().split())
res = 0
for i in range(n):
    if a[i] == res:
        continue
    res += 1
print(res)
