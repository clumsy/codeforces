n, k = (int(i) for i in input().split())
res = []
for i in range(2, n):
    while len(res) < k - 1 and n % i == 0:
        n //= i
        res.append(i)
    if n < i:
        break
    if len(res) == k - 1:
        break
if n > 1:
    res.append(n)
if len(res) != k:
    res = [-1]
print(*res)
