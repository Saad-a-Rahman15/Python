member_amount = input("How many family members do you have? \n")
member_amount = int(member_amount)

members_list = [    ]

for a in range(0, member_amount):
    member = input("Enter member name: \n")
    members_list.append(member)

print("Your family members are: \n")
for noun in members_list:
    print(noun)