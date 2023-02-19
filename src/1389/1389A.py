t = int(input())
for _ in range(t):
    lt, rt = (int(i) for i in input().split())
    res = (lt, 2 * lt) if 2 * lt <= rt else (-1, -1)
    print(*res)
