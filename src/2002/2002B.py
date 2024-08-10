t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    res = "Bob"
    lo, hi = 0, n - 1
    for i in a:
        if b[lo] == i:
            lo += 1
        elif b[hi] == i:
            hi -= 1
        else:
            res = "Alice"
            break
    lo, hi = 0, n - 1
    for i in a[::-1]:
        if b[lo] == i:
            lo += 1
        elif b[hi] == i:
            hi -= 1
        else:
            res = "Alice"
            break
    print(res)
