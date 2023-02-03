t = int(input())
for _ in range(t):
    n, a = int(input()), (i for i in input().split())
    res = n if len(set(a)) == 1 else 1
    print(res)
