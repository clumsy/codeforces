try:
    while s := input():
        res = "NO" if s == "Is it rated?" else "YES"
        print(res, flush=True, end="\n")
except EOFError:
    pass
