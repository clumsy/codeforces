q = int(input())
for _ in range(q):
    n, s = int(input()), input()
    i, res = n - 1, []
    while i >= 0:
        if s[i] == "0":
            d = 2
            i -= 2
        else:
            d = 1
        res.append(chr(ord("a") + int(s[i : i + d]) - 1))
        i -= 1
    res = "".join(res[::-1])
    print(res)
