t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    me = input()
    res = 1 + sum(input() == me for _ in range(n - 1))
    print(res)
