t = int(input())
for _ in range(t):
    s = input()
    hh, mm = (int(c.lstrip("0") or 0) for c in s.split(":"))
    res = (
        ":".join(
            f"{str(i):0>2}" for i in (12 if hh == 0 else hh - 12 if hh > 12 else hh, mm)
        )
        + " "
        + ("PM" if hh >= 12 else "AM")
    )
    print(res)
