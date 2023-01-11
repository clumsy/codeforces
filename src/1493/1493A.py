t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = [i for i in range((k + 1) // 2, k)] + [i for i in range(k + 1, n + 1)]
    print(len(res))
    if res:
        print(*res)
