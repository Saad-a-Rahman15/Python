question1 = input("Do you want to start this counter? Write 1 for 'yes' and 2 for 'no.'  ")

if question1 == "1":
    for number in range(1, 101, 2):
        print(number)

elif question1 == "2":
    print("Okay! Have a nice day!")

else:
    print("That is not the answer '1' or '2'  :(")