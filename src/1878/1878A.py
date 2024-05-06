t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = "NO"
    for i in a:
        if i == k:
            res = "YES"
    print(res)
