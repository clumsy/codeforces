n = input()
res, fours = "YES", 3
for c in n:
    if c in "14":
        fours = 0 if c == "1" else fours + 1
        if fours < 3:
            continue
    res = "NO"
    break
print(res)
