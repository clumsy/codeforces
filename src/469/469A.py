n = int(input())
x = (int(i) for i in input().split())
next(x)
y = (int(i) for i in input().split())
next(y)
res = set(x).union(set(y))
res = "I become the guy." if len(res) == n else "Oh, my keyboard!"
print(res)
