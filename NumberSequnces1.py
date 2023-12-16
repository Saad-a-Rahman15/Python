for a in range(1, 11):
    if ((a % 5 == 0) or (a % 10 == 0)):
        continue
    print(a * a * a)