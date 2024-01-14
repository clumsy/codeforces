n = int(input())
a = [int(i) for i in input().split()]
xor = [0] * (n + 1)
for i in range(1, n + 1):
    xor[i] = a[i - 1] ^ xor[i - 1]
res = 0
for i in range(n + 1):
    for j in range(i, n + 1):
        cur = xor[j] ^ xor[i]
        res = max(res, cur)
print(res)
