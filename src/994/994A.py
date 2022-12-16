n, m = (int(i) for i in input().split())
x = (int(i) for i in input().split())
y = set(int(i) for i in input().split())
res = [i for i in x if i in y]
print(*res)
