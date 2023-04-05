password, n = input(), int(input())
res = "NO"
starts, ends = False, False
for _ in range(n):
    s = input()
    starts = starts or s[0] == password[1]
    ends = ends or s[1] == password[0]
    if s == password or (starts and ends):
        res = "YES"
print(res)
