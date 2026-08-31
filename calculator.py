print("-----Simple Calculator-----")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operation= int(input("Enter Number for the required operation:\n1 = Addition\n2 = Subtraction\n3 = Multiplication\n4 = Division\nNumber : "))
match operation:
    case 1:
        print(f"The Sum of {num1} and {num2} is\n{num1} + {num2} = ", num1+num2 )
    case 2:
        print(f"The Subtraction of {num1} and {num2} is\n{num1} - {num2} = ", num1-num2 )
    case 3:
        print(f"The Multiplication of {num1} and {num2} is\n{num1} * {num2} = ", num1*num2 )
    case 4:
        print(f"The Division of {num1} and {num2} is\n{num1} / {num2} = ", num1/num2 )
    case _:
        print("INVALID\nPlease Enter Numbers From 1 to 4")