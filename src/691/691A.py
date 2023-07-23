n, a = int(input()), (int(i) for i in input().split())
res = "YES" if sum(b == 1 for b in a) == (n - 1 if n > 1 else 1) else "NO"
print(res)
