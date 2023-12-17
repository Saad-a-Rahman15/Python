amount_number = input("How many numbers so you want in your list: \n")
amount_number = int(amount_number) 

odd_list = []

even_list = []

for index in range(0, amount_number):
    number = input("Enter number: \n")
    number = int(number)

    if number % 2 != 0:
        odd_list.append(number)
    else:
        even_list.append(number)

odd = len(odd_list)
print("There are " + str(odd) + " odd numbers.")

even = len(even_list)
print("There are " + str(even) + " even numbers.")