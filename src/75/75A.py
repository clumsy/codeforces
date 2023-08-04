a, b = (input() for _ in range(2))


def process(x):
    return int(x.replace("0", ""))


res = "YES" if process(a) + process(b) == process(str(int(a) + int(b))) else "NO"
print(res)
