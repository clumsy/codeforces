t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = sum(i if i >= 0 else -i for i in a)
    print(res)
