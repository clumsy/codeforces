t = int(input())
for _ in range(t):
    s = input()
    res = (
        "FILIPINO"
        if s[-2:] == "po"
        else "JAPANESE"
        if s[-4:] in ["desu", "masu"]
        else "KOREAN"
        if s[-5:] == "mnida"
        else None
    )
    print(res)
