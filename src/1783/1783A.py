t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = sorted(a, reverse=True)
    res[1], res[-1] = res[-1], res[1]
    if res[0] == res[1]:
        print("NO")
    else:
        print("YES")
        print(*res)
