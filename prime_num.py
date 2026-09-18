def isPrime(num):
    if num <=1 :
        return False

    for i in range (2,num):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if isPrime(num):
    print("It's a prime number")
else :
    print("It's not a prime number")

