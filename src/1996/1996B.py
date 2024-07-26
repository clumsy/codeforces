t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    for i in range(n):
        if i % k != 0:
            input()
            continue
        res = "".join(input()[::k])
        print(res)
