t = int(input())
for _ in range(t):
    n, h = int(input()), (int(i) for i in input().split())
    res = "YES"
    carry = 0
    for i, e in enumerate(h):
        if e + carry >= i:
            carry = e + carry - i
        else:
            res = "NO"
            break
    print(res)
