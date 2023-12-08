a, b, c = (int(i) for i in input().split())
res = "NO"
for i in range(c // a + 1):
    if (c - a * i) % b == 0:
        res = "YES"
        break
print(res)
