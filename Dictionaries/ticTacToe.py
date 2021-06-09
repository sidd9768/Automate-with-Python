theBoard = {'top-L': " ", 'top-M': " ", 'top-R': " ", 'mid-L': " ", 'mid-M': " ", 'mid-R': " ",
'low-L': " ", 'low-M': " ", 'low-R': " "}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def isWinner(board, player):
    """Return True if player is a winner on this TTTBoard."""
    b, p = board, player # Shorter names as "syntactic sugar".
    # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
    return ((b['top-L'] == b['top-M'] == b['top-R'] == p) or # Across the top
            (b['mid-L'] == b['mid-M'] == b['mid-R'] == p) or # Across the middle
            (b['low-L'] == b['low-M'] == b['low-R'] == p) or # Across the bottom
            (b['top-L'] == b['mid-L'] == b['low-L'] == p) or # Down the left
            (b['top-M'] == b['top-M'] == b['low-M'] == p) or # Down the middle
            (b['top-R'] == b['mid-R'] == b['low-R'] == p) or # Down the right
            (b['top-R'] == b['mid-M'] == b['low-L'] == p) or # Diagonal
            (b['top-L'] == b['mid-M'] == b['low-R'] == p))   # Diagonal


def gameFunction():
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)
        print("Turn for " + turn + '. Move on which Space? (leave black to exit)')
        move = input()
        if move == '':
            break
        else:
            if theBoard[move] == " ":
                theBoard[move] = turn
                if isWinner(theBoard, turn):
                    print(turn + ' has won the game!')
                    break
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
            else:
                print('\nXX-- Wrong move selected --XX\n')
                break

gameFunction()
printBoard(theBoard)
