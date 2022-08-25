from itertools import repeat

t = int(input())
for _ in range(t):
    n = int(input())
    s = "".join(repeat("21", times=n // 3))
    if n % 3 == 2:
        s = s + "2"
    elif n % 3 == 1:
        s = "1" + s
    print(s)
