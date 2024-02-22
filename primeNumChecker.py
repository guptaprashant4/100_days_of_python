import math


def prime_checker(number):
    
    is_prime = True
    sqrt_num = math.sqrt(number)
    highest_divisor = math.floor(sqrt_num)

    for num in range(2, highest_divisor + 1):
        if(number % num == 0):
            is_prime = False

    return is_prime

usr_in = int(input("Enter a number: "))
if(prime_checker(usr_in)):
    print("It's a prime number.")
else:
    print("It's not a prime number.")