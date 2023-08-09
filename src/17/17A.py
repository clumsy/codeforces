n, k = (int(i) for i in input().split())
prime = [True] * 1001
prime[1] = False
for i in range(2, len(prime)):
    for j in range(2, i + 1):
        if i * j >= len(prime):
            break
        prime[i * j] = False
res, prv = 0, None
for i in range(2, n):
    if prime[i]:
        if prv and prv + i + 1 > n:
            break
        res += prime[prv + i + 1] if prv else 0
        prv = i
res = "YES" if res >= k else "NO"
print(res)
