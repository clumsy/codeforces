t = int(input())
for _ in range(t):
    n, s = int(input()), input().lower()
    res, meow = "NO", []
    for c in s:
        if not meow or meow[-1] != c:
            meow.append(c)
        if len(meow) > 4:
            break
    res = "YES" if "".join(meow) == "meow" else "NO"
    print(res)
