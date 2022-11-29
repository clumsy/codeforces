t = int(input())
for _ in range(t):
    lft, _ = (int(i) for i in input().split())
    res = lft, 2 * lft
    print(*res)
