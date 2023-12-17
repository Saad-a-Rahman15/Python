print("km to mile")
print("mile to km")
print("kg to lb")
print("lb to kg")
print("Celcius to Farenhiet")
print("Farenhiet to Celcius")
question1 =  input("Choose one of the following:")

if question1 == "km to mile":
    km = input("Choose a number:\n")
    print(int(km) * 0.6)

elif question1 == "mile to km":
    mile = input("Choose a number:\n")
    print(int(mile) * 1.6)

elif question1 == "kg to lb":
    kg = input("Choose a number:\n")
    print(int(kg) * 2.2)

elif question1 == "lb to kg":
    lb = input("Choose a number:\n")
    print(int(lb) * 0.4)

elif question1 == "Celcius to Farenhiet":
    celcius = input("Choose a number:\n")
    print(int(celcius ) * 32)

elif question1 == "Farenhiet to Celcius":
    farenhiet = input("Choose a number:\n")
    print(int(farenhiet) * -17.7)