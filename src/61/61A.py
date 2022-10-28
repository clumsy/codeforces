f, s = input(), input()
res = "".join("1" if fi != si else "0" for fi, si in zip(f, s))
print(res)
