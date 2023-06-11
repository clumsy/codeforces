n, d = (int(i) for i in input().split())
a = sorted(int(i) for i in input().split())
m = int(input())
res = sum(a[: min(n, m)]) - max(0, m - n) * d
print(res)
