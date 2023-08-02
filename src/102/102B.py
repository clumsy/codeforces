n = input()
res = 0
while len(n) > 1:
    n = str(sum(int(i) for i in n))
    res += 1
print(res)
