t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    s = input()
    b = s.count("B")
    if b > k:
        for i, c in enumerate(s):
            b -= c == "B"
            if b == k:
                res = i + 1
                break
        print("1")
        print(res, "A")
    elif b < k:
        for i, c in enumerate(s):
            b += c == "A"
            if b == k:
                res = i + 1
                break
        print("1")
        print(res, "B")
    else:
        res = 0
        print(res)
