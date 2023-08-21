# ----------------------------------------------------------
from random import choice
# ----------------------------------------------------------
with open('practice2.txt', 'r') as f:
    randomWords = f.readlines()
# ----------------------------------------------------------
word = choice(randomWords)[:-1]
wordList = []
guesses = []
run = True
allowedErrors = len(word)
# ----------------------------------------------------------
for _ in range(len(word)):
    wordList.append('_')

for i in wordList:
    print(i, end=' ')
# ----------------------------------------------------------
while run:
    guess = input('\nEnter guess: ')
    guesses.append(guess)
    for letter in word:
        if letter in guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print(f'\n{allowedErrors} allowed errors left.')
    if guess not in word:
        allowedErrors -= 1
        if allowedErrors == 0:
            break
    run = False
    for letter in word:
        if letter not in guesses:
            run = True
# ----------------------------------------------------------
if not run:
    print(f'You found the word. It was {word}')
else:
    print(f'You did not guess the word. It was {word}')
# ----------------------------------------------------------