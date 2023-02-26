t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    c = 1
    for i in a:
        if i == c:
            c += 1
    res = (n - c + 1 + k - 1) // k
    print(res)
