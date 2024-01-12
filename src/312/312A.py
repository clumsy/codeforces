n = int(input())
for _ in range(n):
    s = input()
    miao = s.startswith("miao.")
    lala = s.endswith("lala.")
    if miao == lala:
        res = "OMG>.< I don't know!"
    elif miao:
        res = "Rainbow's"
    elif lala:
        res = "Freda's"
    print(res)
