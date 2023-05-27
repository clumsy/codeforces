t = int(input())
for _ in range(t):
    s = input()
    if "aa" in s or "bb" in s or "cc" in s:
        res = -1
    else:
        res, b, n = list(s), -1, len(s)
        while b < len(s):
            i = b + 1
            while i < n and res[i] == "?":
                i += 1
            while b + 1 < n and res[b + 1] == "?" and b < i:
                cancel = set(res[b])
                if i < n:
                    cancel.add(res[i])
                res[b + 1] = list({"a", "b", "c"} - cancel)[0]
                b += 1
            b += 1
        res = "".join(res)
    print(res)
