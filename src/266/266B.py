n, t = (int(i) for i in input().split())
s = [c for c in input()]
while t:
    i = n - 2
    while i >= 0:
        if s[i : i + 2] == ["B", "G"]:
            s[i : i + 2] = ["G", "B"]
            i -= 2
        else:
            i -= 1
    t -= 1
res = "".join(s)
print(res)
