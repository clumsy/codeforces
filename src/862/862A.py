n, x = (int(i) for i in input().split())
a = set(int(i) for i in input().split())
s = sum(i < x for i in a)
res = abs(x - s) + (x in a)
print(res)
