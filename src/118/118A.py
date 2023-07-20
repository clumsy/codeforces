s = input().lower()
res = "".join(
    c
    for c1, c2 in zip("." * len(s), (x for x in s if x not in "aoeiuy"))
    for c in (c1, c2)
)
print(res)
