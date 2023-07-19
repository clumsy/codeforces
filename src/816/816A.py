s = [int(i.lstrip("0") or "0") for i in input().split(":")]
res, s = 0, 60 * s[0] + s[1]


def is_palindrome(m):
    hh, mm = divmod(m, 60)
    hh %= 24
    return hh // 10 == mm % 10 and hh % 10 == mm // 10


while not is_palindrome((s + res) % (60 * 60)):
    res += 1
print(res)
