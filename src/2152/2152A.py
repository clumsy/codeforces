t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = 2 * len(set(a)) - 1
    print(res)
