s = input()
res = sum(
    c in {"a", "e", "i", "o", "u"} or (c.isdigit() and int(c) & 1 == 1) for c in s
)
print(res)
