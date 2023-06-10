n, s = int(input()), input()
res = "NO"
for i in range(1, n):
    if s[i] < s[i - 1]:
        res = "YES"
        lo, hi = i, i + 1
        break
print(res)
if res == "YES":
    print(lo, hi)
