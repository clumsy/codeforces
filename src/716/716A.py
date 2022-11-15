n, c = (int(i) for i in input().split())
t = [int(i) for i in input().split()]
res = 1
for i in reversed(range(n - 1)):
    if t[i + 1] - t[i] > c:
        break
    res += 1
print(res)
