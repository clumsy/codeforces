t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = (sum(a) + n - 1) // n
    print(res)
