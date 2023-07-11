s = input()
res = "YES" if "1" in s and s[s.find("1") :].count("0") > 5 else "NO"
print(res)
