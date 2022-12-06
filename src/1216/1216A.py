n, s = int(input()), [c for c in input()]
c = 0
for i in range(0, n, 2):
    if s[i] == s[i + 1]:
        s[i] = "b" if s[i + 1] == "a" else "a"
        c += 1
res = "".join(s)
print(c)
print(res)
