a, b, c, n = (int(i) for i in input().split())
diff = a + b - c
res = n - diff if n - diff > 0 and c <= a and c <= b and a <= n and b <= n else -1
print(res)
