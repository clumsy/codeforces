t = int(input())
for _ in range(t):
    for _ in range(3):
        s = input()
        if "?" in s:
            res = "".join(set("ABC") - (set(c for c in s if c != "?")))
    print(res)
