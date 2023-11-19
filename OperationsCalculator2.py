print("Welcome to this python-based calculator!!!")

input1 = input("Choose a number \n")
input2 = input("Choose another number \n")

print("  +  -  *  /  ")


operation_chooser = input("Choose an operation: \n")

if operation_chooser == "+":
    print("Your answer is")
    print(int(input1) + int(input2))
    
elif operation_chooser == "-":
    print("Your answer is")
    print(int(input1) - int(input2))

elif operation_chooser == "*":
    print("Your answer is")
    print(int(input1) * int(input2))

elif operation_chooser == "/":
    if input2 == "0":
        print("You cannot divide anything by 0 :[  ")
    else:
        print("Your answer is")
        print(int(input1) / int(input2))

else:
    print("That is not possible :[ ")