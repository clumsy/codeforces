n = int(input())
c = [int(i) for i in input().split()]
last = []
for i in range(n)[::-1]:
    if not last or c[i] != c[last[0]]:
        last.append(i)
    if len(last) > 1:
        break
res = 0
for i in range(n):
    cur = last[0] - i if c[i] != c[last[0]] else last[1] - i
    res = max(res, cur)
print(res)
