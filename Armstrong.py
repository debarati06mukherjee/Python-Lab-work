def checkArmstrong(n):
    original = n
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit ** 3
        n = n // 10

    if total == original:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if checkArmstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")