s, e = input(), input()
m = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
}
res = "YES" if any((m[e] - m[s]) % 7 == d % 7 for d in [28, 31, 30]) else "NO"
print(res)
