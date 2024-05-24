n, x, y = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
days = set(a[:y])
for i, e in enumerate(a):
    if i + y < n:
        days.add(a[i + y])
    if i >= x + y + 1:
        days.remove(a[i - x])
    if min(days) == a[i]:
        res = i + 1
        break
print(res)
