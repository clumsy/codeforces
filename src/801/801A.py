s = input()
s = "K" + s if s.startswith("KK") else s + "V" if s.endswith("VV") else s
res = s.count("VK") + ("VVV" in s or "KKK" in s)
print(res)
