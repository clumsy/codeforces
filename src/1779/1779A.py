t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = 0 if "RL" in s else i + 1 if (i := s.find("LR")) >= 0 else -1
    print(res)
