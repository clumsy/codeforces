t = int(input())
for _ in range(t):
    A, B, n = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    def strength(i):
        return a[i]

    res = "YES"
    order = sorted(range(n), key=strength)
    for i in order:
        hero_lasts = (B + a[i] - 1) // a[i]
        monster_lasts = (b[i] + A - 1) // A
        if monster_lasts > hero_lasts:
            res = "NO"
            break
        B -= a[i] * monster_lasts
    print(res)
