t = int(input())
for _ in range(t):
    n, r = int(input()), input().split()
    # always send 1 and 3 to one server, 2 to the other
    res = n - sum(i == "2" for i in r)
    print(res)
