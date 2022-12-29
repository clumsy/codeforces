n, s = int(input()), input()
res = "".join(["1" if s[0] == "1" else ""] + ["0"] * s.count("0"))
print(res)
