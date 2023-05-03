keys = "qwertyuiopasdfghjkl;zxcvbnm,./"
o, s = (input() for _ in range(2))
m = {k: v for k, v in zip(keys, keys[1:] if o == "L" else " " + keys)}
res = "".join(m[c] for c in s)
print(res)
