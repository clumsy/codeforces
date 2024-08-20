t = int(input())
for _ in range(t):
    n = int(input())
    res = [input().index("#") + 1 for _ in range(n)][::-1]
    print(*res)
