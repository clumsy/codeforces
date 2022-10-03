t = int(input())
for _ in range(t):
    n, a = int(input()), sum(int(i) for i in input().split())
    res = a - n if a >= n else 1
    print(res)
