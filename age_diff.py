print("age category")
age = int(input("Enter your age"))

if age<13:
    print("you are a child")
elif 13<=age<=19: #can be <20 but for learning purpose using this syntax
    print("teenager")
elif 20<=age<=59:
    print("adult")
else:
    print("senior citizen")

