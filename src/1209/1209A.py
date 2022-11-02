n, a = int(input()), sorted(int(i) for i in input().split())
res = 0
for i in range(n):
    if a[i] > 0:
        for j in range(i + 1, n):
            if a[j] > 0 and a[j] % a[i] == 0:
                a[j] = 0
        res += 1
print(res)
