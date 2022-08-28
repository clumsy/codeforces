t = int(input())
for _ in range(t):
    _, a = input(), sorted([int(i) for i in input().split()])
    b, r = a[0], 0
    for i in range(1, (len(a) + 1) // 2):
        b, r = b + a[i], r + a[-i]
        if r > b:
            break
    print("YES" if r > b else "NO")
