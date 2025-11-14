t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = input()
    res = cur = 0
    for i in a:
        if i == "1":
            res += cur == 0
            cur = k - 1
        else:
            cur = max(0, cur - 1)
    print(res)
