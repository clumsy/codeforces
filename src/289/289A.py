n, k = (int(i) for i in input().split())
s = 0
for _ in range(n):
    a, b = (int(i) for i in input().split())
    s += b - a + 1
a = (s + k - 1) // k
res = abs(a * k - s)
print(res)
