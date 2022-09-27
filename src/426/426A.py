n, s = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
res = "YES" if s >= sum(a) - max(a) else "NO"
print(res)
