n, h = (int(i) for i in input().split())
a = (int(i) for i in input().split())
res = sum(1 if i <= h else 2 for i in a)
print(res)
