import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,_-"

all = lower + upper + numbers + symbols
while True:
    try:
        length = 16#int(input("Enter Length of Password: "))
        if length > 74:
            print("Please select a number equal to or less than 74.")
        else:
            break
    except ValueError:
        print("Please enter a number.")

password = "".join(random.sample(all, length))

print(f"Your password is {password}")