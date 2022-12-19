n, s = int(input()), input()
e = sum(i == "8" for i in s)
ne = n - e
res = 0
while e:
    e -= 1
    if ne > 9:
        ne -= 10
        res += 1
    elif e + ne > 9:
        e -= 10 - ne
        ne = 0
        res += 1
    else:
        break
print(res)
