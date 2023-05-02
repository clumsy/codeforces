m, k = input(), int(input())
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
m2n = {m: i for i, m in enumerate(months)}
res = months[(m2n[m] + k) % 12]
print(res)
