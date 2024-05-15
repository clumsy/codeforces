t = int(input())
for _ in range(t):
    s = input()
    for i, c in enumerate(s):
        if c != s[0]:
            print("YES")
            print(s[i] + s[:i] + s[i + 1 :])
            break
    else:
        print("NO")
