t = int(input())
for _ in range(t):
    px, py = (int(i) for i in input().split())
    s = input()
    counts = {c: 0 for c in "ULDR"}
    for c in s:
        counts[c] += 1
    res = (
        "YES"
        if (
            abs(py) <= counts["U" if py > 0 else "D"]
            and abs(px) <= counts["R" if px > 0 else "L"]
        )
        else "NO"
    )
    print(res)
