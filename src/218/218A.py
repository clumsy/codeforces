n, k = (int(i) for i in input().split())
n = 2 * n + 1
r = [int(i) for i in input().split()]
for i in range(1, n, 2):
    if r[i - 1] < r[i] - 1 > r[i + 1]:
        r[i] -= 1
        k -= 1
        if k == 0:
            break
res = r
print(*res)
