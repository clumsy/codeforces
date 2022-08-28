t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    res, zeroes, s, dupes = 0, 0, set(), False
    for i in a:
        if i == 0:
            zeroes += 1
        elif i in s:
            dupes = True
        else:
            s.add(i)
    if zeroes > 0:
        print(n - zeroes)
    else:
        print(n if dupes else n + 1)
