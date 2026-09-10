print("~~~~Calculating Leap Year~~~~")
year = int(input("Enter a year: "))
if len(str(year)) != 4:
    print("PLease enter a year with 4 digit")
else:
    if year%400 == 0:
        print ("It's a leap Year")
    elif year%4 == 0:
        print("It's a leap year")
    elif year%100 == 0:
        print("It's a leap year")
    else:
        print("It's not a leap year")