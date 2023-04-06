s = input()


def rotate(s, i):
    n = len(s)
    return s[n - i :] + s[: n - i]


res = len(set(rotate(s, i) for i in range(len(s))))
print(res)
