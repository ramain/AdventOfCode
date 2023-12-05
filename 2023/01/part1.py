f = open("input", "r")

cal = 0
for line in f:
    n = ''.join(x for x in line if x.isdigit())
    if len(n) > 2:
        n = n[0] + n[-1]
    if len(n) == 1:
        n = n + n
    n = int(n)
    cal += n
    print(n)
print(cal)
