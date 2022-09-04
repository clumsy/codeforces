for r in range(5):
    c = input().find("1") // 2
    if c >= 0:
        res = abs(r - 2) + abs(c - 2)
        print(res)
        break
