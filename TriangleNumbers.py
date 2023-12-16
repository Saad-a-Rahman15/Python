first_number = 1

for a in range(1, 100):
    if a == 1:
        print(first_number)
        continue
    first_number = first_number + a
    print(first_number)
    