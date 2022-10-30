n, a = int(input()), [int(i) for i in input().split()]
mi, ma, res = min(a), max(a), 0
for i in range(n):
    if a[i] == ma:
        res += i
        while i > 0:
            a[i], a[i - 1] = a[i - 1], a[i]
            i -= 1
        break
for i in reversed(range(n)):
    if a[i] == mi:
        res += n - 1 - i
        break
print(res)
