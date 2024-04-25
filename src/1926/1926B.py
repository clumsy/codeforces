t = int(input())
for _ in range(t):
    prv, n, res = 0, int(input()), "TRIANGLE"
    for _ in range(n):
        s = input()
        cnt = s.count("1")
        if cnt and prv and cnt == prv:
            res = "SQUARE"
        prv = cnt
    print(res)
