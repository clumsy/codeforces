n, s = int(input()), input()
L = s.count("L")
o = n - L
l1 = o1 = 0
res = -1
for i in range(len(s) - 1):
    l1 += s[i] == "L"
    o1 += s[i] == "O"
    if l1 != L - l1 and o1 != o - o1:
        res = i + 1
        break
print(res)
