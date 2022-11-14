n, s = int(input()), input()
z = s.count("0")
if 2 * z != n:
    print(1)
    print(s)
else:
    print(2)
    print(s[0], s[1:])
