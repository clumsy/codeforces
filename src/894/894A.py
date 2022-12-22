s = input()
ql, qr = 0, s.count("Q")
res = 0
for c in s:
    if c == "Q":
        ql += 1
        qr -= 1
    elif c == "A":
        res += ql * qr
print(res)
