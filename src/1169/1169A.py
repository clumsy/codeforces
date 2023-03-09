n, a, x, b, y = (int(i) for i in input().split())
res = "NO"
a, x, b, y = a - 1, x - 1, b - 1, y - 1
while a != x and b != y and a != b:
    a = (a + 1) % n
    b = (b - 1) % n
res = "YES" if a == b else "NO"
print(res)
