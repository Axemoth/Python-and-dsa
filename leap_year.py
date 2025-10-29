print("Leap year Checker")
year = int(input("Enter a year"))

if (year%400 == 0) or (year%4 == 0 and year%100 !=0):
    print("Its a leap year")
else:
    print("Its not a leap year")