t = int(input())
for _ in range(t):
    k = int(input())
    # x! + (x - 1)! = k
    # (x - 1)! * (x + 1) = k
    # x + 1 = k => x = k - 1
    res = k - 1
    print(res)
