s = input()
dot = s.find(".")
i, d = s[dot - 1], s[dot + 1]
res = "GOTO Vasilisa." if i == "9" else int(s[:dot]) + (int(d) >= 5)
print(res)
