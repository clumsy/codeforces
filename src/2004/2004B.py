t = int(input())
for i in range(t):
    al, ar = (int(i) for i in input().split())
    bl, br = (int(i) for i in input().split())
    if al > bl:
        al, ar, bl, br = bl, br, al, ar
    if br <= ar:
        res = br - bl + (al != bl) + (ar != br)
    elif bl <= ar:
        res = ar - bl + 1 + (al != bl)
    else:
        res = 1
    print(res)
