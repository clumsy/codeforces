n, a = int(input()), sorted(int(i) for i in input().split())
m, q = int(input()), (int(i) for i in input().split())
s = sum(a)
for _ in range(m):
    res = s - a[-next(q)]
    print(res)
