n, s = int(input()), input()
r = [0] * 10
for c in s:
    if c >= "0" and c <= "9":
        r[int(c)] = 0
    else:
        it = range(len(r))
        for i in it if c == "L" else reversed(it):
            if not r[i]:
                r[i] = 1
                break
res = "".join(str(i) for i in r)
print(res)
