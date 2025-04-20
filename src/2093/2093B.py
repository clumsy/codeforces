t = int(input())
for _ in range(t):
    n = list(input())
    res = 0
    while n[-1] == "0":
        n.pop()
        res += 1
    for i in n[:-1]:
        res += i != "0"
    print(res)
