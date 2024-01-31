lft, rgt = input().split("|")
rem = input()
hlf, r = divmod(len(lft) + len(rgt) + len(rem), 2)
if r > 0 or hlf < max(len(lft), len(rgt)):
    res = "Impossible"
else:
    mi = hlf - len(lft)
    res = f"{lft + rem[:mi]}|{rgt + rem[mi:]}"
print(res)
