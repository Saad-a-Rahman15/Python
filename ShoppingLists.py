item_number = input("How many items do you want on your shopping list? \n")
item_number = int(item_number)

shopping_list = [   ]

for i in range(0, item_number):
    item = input("Enter item name: \n")
    shopping_list.append(item)

print("Your shopping list contains: \n")   
for noun in shopping_list:
    print(noun)
