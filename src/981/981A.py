s = input()


def palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True


n = len(s)
if not palindrome(s):
    res = n
else:
    res = n - 1
    while res > 0:
        if any(not palindrome(s[i : i + res]) for i in range(n - res)):
            break
        res -= 1
print(res)
