s = input()
res = "YES" if s == s[::-1] and all(c in "AHIMOTUVWXY" for c in s) else "NO"
print(res)
