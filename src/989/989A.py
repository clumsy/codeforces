s = input()
res = "NO"
for i in range(len(s) - 2):
    if "".join(sorted(s[i : i + 3])) == "ABC":
        res = "YES"
        break
print(res)
