k = int(input())
d, r = divmod(max(0, k - 4), 3)
print("+------------------------+")
for i in range(4):
    lst = "O." if k > i else "#."
    occ = d + (r > min(i, 2)) if i != 2 else 0
    avl = 10 - occ
    occ = "O." * occ if i != 2 else ""
    avl = ("#." if i != 2 else "..") * avl
    drv = "|D|" if i == 0 else "..|" if i == 2 else "|.|"
    hdl = ")" if i == 0 or i == 3 else ""
    print(f"|{lst}{occ}{avl}{drv}{hdl}")
print("+------------------------+")
