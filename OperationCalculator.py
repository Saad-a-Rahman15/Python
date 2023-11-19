print("Welcome to this python-based calculator!!!")
name1 = input("Hi, What's your name?\n")

print("   +    -    *    /")
question_starter = input("Choose an operation from above " + name1 + " :\n")
print("PLEASE WRITE YOUR ANSWER CORRECTLY!!!") #This is important so that the file dosen't crash
reply1 = "+"
reply2 = "-"
reply3 = "*"
reply4 = "/"

if question_starter == reply1:
    add1 = input("Choose a number:\n")
    add2 = input("Choose a number that you want to add with " + add1 + " :\n")
    print(name1 + ", your answer is")
    print(int(add1) + int(add2))

elif question_starter == reply2:
    minus1 = input("Choose a number:\n")
    minus2 = input("Choose a number that you want to  with " + minus1 + " :\n")
    print(name1 + ", your answer is")
    print(int(minus1) - int(minus2))

elif question_starter == reply3:
    times1 = input("Choose a number:\n")
    times2 = input("Choose a number that you want to  with " + times1 + " :\n")
    print(name1 + ", your answer is")
    print(int(times1) * int(times2))

elif question_starter == reply4:
    divide1 = input("Choose a number:\n")
    divide2 = input("Choose a number that you want to  with " + divide1 + " :\n")
    print(name1 + ", your answer is")
    print(int(divide1) / int(divide2))

else:
    print("Sorry, that is not possible  :[")