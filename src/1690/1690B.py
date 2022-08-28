t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    possible, min_diff, diff = True, -1, -1
    for i in range(n):
        if a[i] - b[i] < 0:
            possible = False
            break
        if b[i] == 0:
            if 0 <= diff < a[i] - b[i]:
                possible = False
                break
            min_diff = max(min_diff, a[i] - b[i])
        else:
            if 0 <= diff != a[i] - b[i] or (min_diff >= 0 and a[i] - b[i] < min_diff):
                possible = False
                break
            diff = a[i] - b[i]
    print("YES" if possible else "NO")
