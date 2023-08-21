import random

minimum = 1
maximum = 100
computers_number = random.randint(minimum, maximum)
prompt = 'Type in your guess: '
number_of_guesses = 0

print(f'Range: {minimum} - {maximum}')

while number_of_guesses <= 10:
    players__guess = input(prompt)
    if number_of_guesses <= 10 and players__guess == computers_number:
        print(f'Correct! The answer was {computers_number}.')
        break
    elif number_of_guesses == 10 and players__guess != computers_number:
        print(f"You ran out of guesses! You loose, LOL! The correct answer was {computers_number}.")
        break
    elif computers_number == int(players__guess):
        print(f'Correct! The answer was {computers_number}')
        break
    elif computers_number > int(players__guess):
        print('Too low')
    else:
        print('Too high')
    number_of_guesses += 1
