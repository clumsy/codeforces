t = int(input())
for _ in range(t):
    s = input()
    possible, keys = True, set()
    for c in s:
        if c.islower():
            keys.add(c)
        elif c.lower() not in keys:
            possible = False
            break
    print("YES" if possible else "NO")
