print("Movie ticket pricing")
age = int(input("Enter your age:"))
week = input("Enter the day of the week:")
'''
if week =="Wednesday":
    if age<18:
        print("Your ticket price is 6 dollars \n Thank you")
    else:
        print("Your ticket price is 10 dollars \n Thank you")
else:
    if age<18:
        print("Your ticket price is 8 dollars \n Thank you")
    else:
        print("Your ticket price is 12 dollars \n Thank you")
'''
price = 12 if age>=18 else 8 

if week =="Wednesday":
    price = price-2

print(f"Your ticket price is {price}")
