# --------------------------------------------------------------------------------------------------------------------------------
board = [
    '_', '_', '_', '_', '_', '_', '_',
    '_', '_', '_', '_', '_', '_', '_',
    '_', '_', '_', '_', '_', '_', '_',
    '_', '_', '_', '_', '_', '_', '_',
    '_', '_', '_', '_', '_', '_', '_',
    '_', '_', '_', '_', '_', '_', '_'
]
# --------------------------------------------------------------------------------------------------------------------------------
def drawBoard():
    for index, space in enumerate(board):
        if (index + 1) % 7 != 0: 
            print(f'{space} |', end = ' ')
        else:
            print(space)
# --------------------------------------------------------------------------------------------------------------------------------
def playerOneMove(bo, bot, mo):
    if bo[bot] == '_' or bo[bot - 7] == '_' or bo[bot - 14] == '_' or bo[bot - 21] == '_' or bo[bot - 28] == '_' or bo[mo] == '_':
        if bo[bot] == '_':
            bo[bot] = 'X'
        elif bo[bot - 7] == '_':
            bo[bot - 7] = 'X'
        elif bo[bot - 14] == '_':
            bo[bot - 14] = 'X'
        elif bo[bot - 21] == '_':
            bo[bot - 21] = 'X'
        elif bo[bot - 28] == '_':
            bo[bot - 28] = 'X'
        elif bo[mo] == '_':
            bo[mo] = 'X'
    else:
        if bo[bot] == 'O' or bo[bot] == 'X':
            bo[bot - 7] = 'X'
        elif bo[bot - 7] == 'O' or bo[bot - 7] == 'X':
            bo[bot - 14] = 'X'
        elif bo[bot - 14] == 'O' or bo[bot - 14] == 'X':
            bo[bot - 21] = 'X'
        elif bo[bot - 21] == 'O' or bo[bot - 21] == 'X':
            bo[bot - 28] = 'X'
        elif bo[bot - 28] == 'O' or bo[bot - 28] == 'X':
            bo[mo] = 'X'
    drawBoard()
# --------------------------------------------------------------------------------------------------------------------------------
def playerTwoMove(bo, bot, mo):
    if bo[bot] == '_' or bo[bot - 7] == '_' or bo[bot - 14] == '_' or bo[bot - 21] == '_' or bo[bot - 28] == '_' or bo[mo] == '_':
        if bo[bot] == '_':
            bo[bot] = 'O'
        elif bo[bot - 7] == '_':
            bo[bot - 7] = 'O'
        elif bo[bot - 14] == '_':
            bo[bot - 14] = 'O'
        elif bo[bot - 21] == '_':
            bo[bot - 21] = 'O'
        elif bo[bot - 28] == '_':
            bo[bot - 28] = 'O'
        elif bo[mo] == '_':
            bo[mo] = 'O'
    else:
        if bo[bot] == 'O' or bo[bot] == 'X':
            bo[bot - 7] = 'O'
        elif bo[bot - 7] == 'O' or bo[bot - 7] == 'X':
            bo[bot - 14] = 'O'
        elif bo[bot - 14] == 'O' or bo[bot - 14] == 'X':
            bo[bot - 21] = 'O'
        elif bo[bot - 21] == 'O' or bo[bot - 21] == 'X':
            bo[bot - 28] = 'O'
        elif bo[bot - 28] == 'O' or bo[bot - 28] == 'X':
            bo[mo] = 'O'
    drawBoard()
# --------------------------------------------------------------------------------------------------------------------------------
def checkRows(bo, le):
    return ((bo[0] == le and bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le and bo[4] == le) or
            (bo[2] == le and bo[3] == le and bo[4] == le and bo[5] == le) or
            (bo[3] == le and bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[7] == le and bo[8] == le and bo[9] == le and bo[10] == le) or
            (bo[8] == le and bo[9] == le and bo[10] == le and bo[11] == le) or
            (bo[9] == le and bo[10] == le and bo[11] == le and bo[12] == le) or
            (bo[10] == le and bo[11] == le and bo[12] == le and bo[13] == le) or
            (bo[14] == le and bo[15] == le and bo[16] == le and bo[17] == le) or
            (bo[15] == le and bo[16] == le and bo[17] == le and bo[18] == le) or
            (bo[16] == le and bo[17] == le and bo[18] == le and bo[19] == le) or
            (bo[17] == le and bo[18] == le and bo[19] == le and bo[20] == le) or
            (bo[21] == le and bo[22] == le and bo[23] == le and bo[24] == le) or
            (bo[22] == le and bo[23] == le and bo[24] == le and bo[25] == le) or
            (bo[23] == le and bo[24] == le and bo[25] == le and bo[26] == le) or
            (bo[24] == le and bo[25] == le and bo[26] == le and bo[27] == le) or
            (bo[28] == le and bo[29] == le and bo[30] == le and bo[31] == le) or
            (bo[29] == le and bo[30] == le and bo[31] == le and bo[32] == le) or
            (bo[30] == le and bo[31] == le and bo[32] == le and bo[33] == le) or
            (bo[31] == le and bo[32] == le and bo[33] == le and bo[34] == le) or
            (bo[35] == le and bo[36] == le and bo[37] == le and bo[38] == le) or
            (bo[36] == le and bo[37] == le and bo[38] == le and bo[39] == le) or
            (bo[37] == le and bo[38] == le and bo[39] == le and bo[40] == le) or
            (bo[38] == le and bo[39] == le and bo[40] == le and bo[41] == le))
# -------------------------------------------------------------------------------------------------------------------------------
def checkColumns(bo, le):
    return ((bo[0] == le and bo[7] == le and bo[14] == le and bo[21] == le) or
            (bo[7] == le and bo[14] == le and bo[21] == le and bo[28] == le) or
            (bo[14] == le and bo[21] == le and bo[28] == le and bo[35] == le) or
            (bo[1] == le and bo[8] == le and bo[15] == le and bo[22] == le) or
            (bo[8] == le and bo[15] == le and bo[22] == le and bo[29] == le) or
            (bo[15] == le and bo[22] == le and bo[29] == le and bo[36] == le) or
            (bo[2] == le and bo[9] == le and bo[16] == le and bo[23] == le) or
            (bo[9] == le and bo[16] == le and bo[23] == le and bo[30] == le) or
            (bo[16] == le and bo[23] == le and bo[30] == le and bo[37] == le) or
            (bo[3] == le and bo[10] == le and bo[17] == le and bo[24] == le) or
            (bo[10] == le and bo[17] == le and bo[24] == le and bo[31] == le) or
            (bo[17] == le and bo[24] == le and bo[31] == le and bo[38] == le) or
            (bo[4] == le and bo[11] == le and bo[18] == le and bo[25] == le) or
            (bo[11] == le and bo[18] == le and bo[25] == le and bo[32] == le) or
            (bo[18] == le and bo[25] == le and bo[32] == le and bo[39] == le) or
            (bo[5] == le and bo[12] == le and bo[19] == le and bo[26] == le) or
            (bo[12] == le and bo[19] == le and bo[26] == le and bo[33] == le) or
            (bo[19] == le and bo[26] == le and bo[33] == le and bo[40] == le) or
            (bo[6] == le and bo[13] == le and bo[20] == le and bo[27] == le) or
            (bo[13] == le and bo[20] == le and bo[27] == le and bo[34] == le) or
            (bo[20] == le and bo[27] == le and bo[34] == le and bo[41] == le))
# -------------------------------------------------------------------------------------------------------------------------------
def checkDiagonals(bo, le):
    return ((bo[14] == le and bo[22] == le and bo[30] == le and bo[38] == le) or
            (bo[7] == le and bo[15] == le and bo[23] == le and bo[31] == le) or
            (bo[15] == le and bo[23] == le and bo[31] == le and bo[39] == le) or
            (bo[0] == le and bo[8] == le and bo[16] == le and bo[24] == le) or
            (bo[8] == le and bo[16] == le and bo[24] == le and bo[32] == le) or
            (bo[16] == le and bo[24] == le and bo[32] == le and bo[41] == le) or
            (bo[1] == le and bo[9] == le and bo[17] == le and bo[25] == le) or
            (bo[9] == le and bo[17] == le and bo[25] == le and bo[33] == le) or
            (bo[17] == le and bo[25] == le and bo[33] == le and bo[41] == le) or
            (bo[2] == le and bo[10] == le and bo[18] == le and bo[26] == le) or
            (bo[10] == le and bo[18] == le and bo[26] == le and bo[34] == le) or
            (bo[3] == le and bo[11] == le and bo[19] == le and bo[27] == le) or
            (bo[20] == le and bo[26] == le and bo[32] == le and bo[38] == le) or
            (bo[13] == le and bo[19] == le and bo[25] == le and bo[31] == le) or
            (bo[19] == le and bo[25] == le and bo[31] == le and bo[37] == le) or
            (bo[6] == le and bo[12] == le and bo[18] == le and bo[24] == le) or
            (bo[12] == le and bo[18] == le and bo[24] == le and bo[30] == le) or
            (bo[18] == le and bo[24] == le and bo[30] == le and bo[36] == le) or
            (bo[5] == le and bo[11] == le and bo[17] == le and bo[23] == le) or
            (bo[11] == le and bo[17] == le and bo[23] == le and bo[29] == le) or
            (bo[17] == le and bo[23] == le and bo[29] == le and bo[35] == le) or
            (bo[4] == le and bo[10] == le and bo[16] == le and bo[22] == le) or
            (bo[10] == le and bo[16] == le and bo[22] == le and bo[28] == le) or
            (bo[3] == le and bo[9] == le and bo[15] == le and bo[21] == le))
# -------------------------------------------------------------------------------------------------------------------------------
def isFull(bo):
    if bo.count('_') == 0:
        return False
    else:
        return True
# -------------------------------------------------------------------------------------------------------------------------------
def main():
    drawBoard()
    player =  1
    while True:
        try:
            if isFull(board):
                move = int(input(f'Player {player}, enter the column (1-7): '))
                if 1 <= move <= 7:
                    move -= 1
                    bottom = move + 35
                    if player == 1:
                        playerOneMove(board, bottom, move)
                        if checkRows(board, 'X') or checkColumns(board, 'X') or checkDiagonals(board, 'X'):
                            print(f'Player {player} has won.')
                            break
                        else:
                            player = 2
                    else:
                        playerTwoMove(board, bottom, move)
                        if checkRows(board, 'O') or checkColumns(board, 'O') or checkDiagonals(board, 'O'):
                            print(f'Player {player} has won.')
                            break
                        else:
                            player = 1
                else:
                    print('Please enter a number between 1-7.')
            else:
                print('Tie Game!')
                break
        except ValueError:
            print('Please enter a number.')
# --------------------------------------------------------------------------------------------------------------------------------
main()
# --------------------------------------------------------------------------------------------------------------------------------
