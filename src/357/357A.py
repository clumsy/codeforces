n = int(input())
a = [int(i) for i in input().split()]
x, y = (int(i) for i in input().split())
res = 0
cur, s = 0, sum(a)
for i in range(n):
    cur += a[i]
    if x <= cur <= y and x <= s - cur <= y:
        res = i + 2
print(res)
