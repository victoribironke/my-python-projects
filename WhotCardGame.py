# ---------------------------------------------------------------------------------------
import random
# ---------------------------------------------------------------------------------------
def createDeck():
    deck = []
    shapes = ['Sq', 'St', 'Cr', 'Ci', 'Tr']
    numbers = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14']
    # -------------------------------------
    for _ in range(52):
        shape = random.choice(shapes)
        number = random.choice(numbers)
        element = f'{number} {shape}'
        deck.append(element)
    # -------------------------------------
    random.shuffle(deck)
    return deck
# ---------------------------------------------------------------------------------------
def remove(deck):
    ele = deck.pop()
    return ele
# ---------------------------------------------------------------------------------------
def help():
    print('You must play a card that has either the same number or the same shape of the card preceeding it')
    print('If you don\'t have a card that meets the requirements, you must pick a card until you do.')
    print('Picking a card means it is your opponent\'s turn to play.')
    print('FIRST TO CLEAR OUT THEIR DECK, WINS!')
# ---------------------------------------------------------------------------------------
class Player:
    def __init__(self, name, cards, cardDeck, playingDeck):
        self.name = name
        self.cards = cards
        self.cardDeck = cardDeck
        self.playingDeck = playingDeck
    # -----------------------------------------------------
    def __str__(self):
        return f'{self.name}: {self.cards}'
    # -----------------------------------------------------
    def pick(self):
        self.cards.append(self.cardDeck.pop())
    # -----------------------------------------------------
    def play(self, index):
        self.playingDeck.append(self.cards.pop(index))
# ---------------------------------------------------------------------------------------
deck = createDeck()
player1 = input('Player 1, enter your name: ')
player2 = input('Player 2, enter your name: ')
numOfCards = int(input('How many cards per person: '))
# --------------------------------------------
player1Cards = []
player2Cards = []
for _ in range(numOfCards):
    player1Cards.append(deck.pop())
    player2Cards.append(deck.pop())
# --------------------------------------------
cards = [deck.pop()]
# --------------------------------------------
playerOne = Player(player1, player1Cards, deck, cards)
playerTwo = Player(player2, player2Cards, deck, cards)
# ---------------------------------------------------------------------------------------
player = 1
print(f'Playing Deck: {cards}')
print(playerOne)
print(playerTwo)
action = input('Do you want to read the rules of the game(y/n): ').lower()
if action == 'y':
    help()
else:
    pass
while True:
    if len(deck) == 0:
        random.shuffle(deck.append(cards.clear()))
    else:
        if player == 1:
            print(f'It\'s {player1}\'s turn.', end=' ')
            action = input('Play or pick(pl/pi)? ').lower()
            if action == 'pl':
                action = int(input('Enter the number corresponding to the card: '))
                action -= 1
                if (player1Cards[action][0] == cards[-1][0] and player1Cards[action][1] == cards[-1][1]) or (player1Cards[action][-1] == cards[-1][-1] and player1Cards[action][-2] == cards[-1][-2]):
                    playerOne.play(action)
                    if len(player1Cards) == 0:
                        print(f'{player1} won the game.')
                        break
                    else:
                        player = 2
                else:
                    print('That is an invalid card.')
            elif action == 'pi':
                playerOne.pick()
                player = 2
        else:
            print(f'It\'s {player2}\'s turn.', end=' ')
            action = input('Play or pick(pl/pi)? ').lower()
            if action == 'pl':
                action = int(input('Enter the number corresponding to the card: '))
                action -= 1
                if (player2Cards[action][0] == cards[-1][0] and player2Cards[action][1] == cards[-1][1]) or (player2Cards[action][-1] == cards[-1][-1] and player2Cards[action][-2] == cards[-1][-2]):
                    playerTwo.play(action)
                    if len(player2Cards) == 0:
                        print(f'{player2} won the game.')
                        break
                    else:
                        player = 1
                else:
                    print('That is an invalid card.')
            elif action == 'pi':
                playerTwo.pick()
                player = 1
        print(f'\nPlaying Deck: {cards}')
        print(playerOne)
        print(f'{playerTwo}\n')