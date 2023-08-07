s, t, j, res = input(), "hello", 0, "NO"
for c in s:
    if c == t[j]:
        j += 1
    if j == len(t):
        res = "YES"
        break
print(res)
