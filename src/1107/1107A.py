q = int(input())
for _ in range(q):
    n, s = int(input()), input()
    if n == 2 and int(s[0]) >= int(s[1]):
        print("NO")
    else:
        print("YES")
        res = s[0], s[1:]
        print(len(res))
        print(*res)
