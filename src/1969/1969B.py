t = int(input())
for _ in range(t):
    s = input()
    res = ones = 0
    for d in s:
        ones += d == "1"
        if d == "0" and ones:
            res += ones + 1
    print(res)
