s = input()
m = {input(): str(i) for i in range(10)}
res = "".join(m[s[i : i + 10]] for i in range(0, len(s), 10))
print(res)
