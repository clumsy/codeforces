with open("input.txt") as f:
    s = f.readline().strip()
    a = int(f.readline().strip())
res = "L" if (s == "front" and a == 1) or (s == "back" and a == 2) else "R"
with open("output.txt", "w") as f:
    print(res, file=f)
