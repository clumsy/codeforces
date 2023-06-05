n, k = (int(i) for i in input().split())
s = list(input())
if n == 1:
    if k >= (s[0] != "0"):
        s = ["0"]
else:
    for i, c in enumerate(s):
        if k == 0:
            break
        if i == 0:
            k -= c != "1"
            s[i] = "1"
        else:
            k -= c != "0"
            s[i] = "0"
res = "".join(s)
print(res)
