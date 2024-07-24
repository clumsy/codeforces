t = int(input())
for _ in range(t):
    n = input()
    res = "YES"
    if len(n) < 3 or n[:2] != "10" or n[2] == "0" or int(n[2:]) < 2:
        res = "NO"
    print(res)
