c1, c2, c3, c4 = (int(i) for i in input().split())
n, m = (int(i) for i in input().split())
a = (int(i) for i in input().split())
b = (int(i) for i in input().split())
x1 = min(sum(min(i * c1, c2) for i in a), c3)
x2 = min(sum(min(i * c1, c2) for i in b), c3)
res = min(x1 + x2, c4)
print(res)
