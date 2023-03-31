t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res, p = 0, -1
    for i, e in enumerate(a):
        if e == 0:
            res += i - p > 1
            if res == 2:
                break
            p = i
    res += n - p > 1
    # can't be more than 2
    # we will always make the span from first 0 to last = w (!= 0)
    # then next span will make it all 0
    res = min(2, res)
    print(res)
