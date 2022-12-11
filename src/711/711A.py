n = int(input())
b = [input() for _ in range(n)]
res = "NO"
for i in range(n):
    if b[i].startswith("OO"):
        b[i] = "++" + b[i][2:]
        res = "YES"
        break
    elif b[i].endswith("OO"):
        b[i] = b[i][:3] + "++"
        res = "YES"
        break
print(res)
if res == "YES":
    print("\n".join(b))
