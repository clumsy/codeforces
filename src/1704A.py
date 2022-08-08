t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    a, b = input(), input()
    rem = len(a) - len(b) + 1
    if len(b) > len(a) or b[1:] != a[rem:]:
        print("NO")
    else:
        print("YES" if b[0] in a[:rem] else "NO")
