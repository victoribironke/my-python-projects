# Board
# Display Board
# Start Game
# Players Name
# Current Player
# Flip Player
# Check Win
    # Check Rows 
    # Check Columns
    # Check Diagonals   

# Check Tie
    # Check Rows 
    # Check Columns
    # Check Diagonals


# ----------- Global Variables -----------

Board = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_']


Game_In_Progress = True

Winner = None

Player_name_1 = input('Please Enter Name of Player 1: ')
Player_name_2 = input('Please Enter Name of Player 2: ')

Current_Player = Player_name_1
Next_Player = Player_name_2


Row_1 = Board[0] == Board[1] == Board[2] != '_'
Row_2 = Board[3] == Board[4] == Board[5] != '_'
Row_3 = Board[6] == Board[7] == Board[8] != '_'


Rows = [Row_1, Row_2, Row_3]

Column_1 = Board[0] == Board[3] == Board[6] != '_'
Column_2 = Board[1] == Board[4] == Board[7] != '_'
Column_3 = Board[2] == Board[5] == Board[8] != '_'

Columns = [Column_1, Column_2, Column_3]


Diagonal_1 = Board[0] == Board[4] == Board[8] != '_'
Diagonal_2 = Board[2] == Board[4] == Board[6] != '_'

Diagonals = [Diagonal_1, Diagonal_2]
# ----------- Functions -----------

def Start_Game():
    global Winner
    if Winner == Player_name_1 or Player_name_2:
        print(Winner)
    elif Winner == None:
        print("Tie.")


def Player():
    Players = [Player_name_1, Player_name_2]


def Board_Display():
    print(Board[0], '|', Board[1], '|', Board[2])
    print(Board[3], '|', Board[4], '|', Board[5])
    print(Board[6], '|', Board[7], '|', Board[8])


def Handel_Play(Current_Player):
    #global Current_Player

    print(Current_Player + "'s Turn")

    Placement = int(input('Take Your Turn from 1-9:'))
    Placement = Placement - 1
    Board[Placement] = "X"

    '''if "X" in Board:
        print(int(input('Already taken. Please try again: ')))
    else:
        return'''


def Check_End_Game():
    Check_for_Win()
    Check_for_Tie()

def Check_for_Win():
    global Winner
    global Game_In_Progress
    global Rows
    global Columns
    global Diagonals
    
    if Check_Rows():
        Winner = Check_Rows()
    elif Check_Columns():
        Winner = Check_Columns()
    elif Check_Diagonals:
        Winner  =  Check_Diagonals()
    else:
        Winner = 'None'


     

def Check_Rows():
    global Game_In_Progress
    global Rows

    Row_1 = Board[0] == Board[1] == Board[2] != '_'
    Row_2 = Board[3] == Board[4] == Board[5] != '_'
    Row_3 = Board[6] == Board[7] == Board[8] != '_'

    Rows=[Row_1, Row_2, Row_3]

    if Row_1 or Row_2 or Row_3:
        Game_In_Progress = False
    if Row_1:
        Board[0]
    if Row_2:
        Board[3]
    if Row_3:
        Board[6]


def Check_Columns():
    global Game_In_Progress
    global Columns

    Column_1 = Board[0] == Board[3] == Board[6] != '_'
    Column_2 = Board[1] == Board[4] == Board[7] != '_'
    Column_3 = Board[2] == Board[5] == Board[8] != '_'

    Columns = [Column_1, Column_2, Column_3]

    if Column_1 or Column_2 or Column_3:
        Game_In_Progress = False
    if Column_1:
        Board[0]
    if Column_2:
        Board[1]
    if Column_3:
        Board[2]
    return

def Check_Diagonals():
    global Game_In_Progress
    global Diagonals

    Diagonal_1 = Board[0] == Board[4] == Board[8] != '_'
    Diagonal_2 = Board[2] == Board[4] == Board[6] != '_'


    Diagonals=[Diagonal_1, Diagonal_2]

    if Diagonal_1 or Diagonal_2:
        Game_In_Progress = False
    if Diagonal_1:
        Board[0]
    if Diagonal_2:
        Board[6]
    return


def Check_for_Tie():
    return


def Flip_Player(Next_Player):
    print(Next_Player + "'s Turn")

    Placement = input('Take Your Turn from 1-9:')
    Placement = int(Placement) - 1
    Board[Placement] = 'O'

    '''if "O" in Board:
        print(int(input("Please try again:")))
    else:
        return

    return'''


    Player()
    Board_Display()
while Game_In_Progress:
    Handel_Play(Current_Player)

    Board_Display()

    Check_End_Game()

    Flip_Player(Next_Player)

    Board_Display()

    Check_End_Game()

Start_Game()