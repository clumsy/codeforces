t = int(input())
for _ in range(t):
    n = input()
    zero = five = -1
    for i, e in enumerate(n[::-1]):
        if e not in ["5", "0"]:
            if five >= 0 and e in ["2", "7"]:  # ...25 or ...75
                # removing (i; five) and (five + 1; -1)
                res = i - 1 - five + five
                break
        elif e == "0":
            if zero >= 0:  # ...00
                # removing (i; zero) and (zero + 1; -1)
                res = i - 1 - zero + zero
                break
            zero = i
        else:
            if zero >= 0:  # ...50
                # removing (i; zero) and (zero + 1; -1)
                res = i - 1 - zero + zero
                break
            five = i
    print(res)
