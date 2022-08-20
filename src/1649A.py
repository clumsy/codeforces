t = int(input())
for _ in range(t):
    _, a = input(), input()
    # checking length of string without 1s on both sides
    res = len("".join(a.split()).strip("1"))
    res += res != 0  # need x + 1 coins to jump over x elements
    print(res)
