t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = 0
    fst = lst = next(a)
    for i in a:
        res += i < lst
        lst = i
    res = "YES" if res == 0 or (res == 1 and lst <= fst) else "NO"
    print(res)
